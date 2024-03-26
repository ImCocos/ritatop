import json
import threading
from typing import Callable

from .. import storage
from .. import models
from .. import sockets
from ...cryptography import core
from ...config import Config


config = Config()
kloader = core.KeyLoader()
private_key = kloader.get_rsa_private_key_from_file(config.private_key_path, config.password)
public_key = kloader.get_rsa_public_key_from_file(config.public_key_path)
cryptor = core.Cryptor(
    config.password,
    kloader,
    private_key,
    public_key
)
if not private_key:
    kloader.write_private_key_to_file(config.private_key_path, cryptor.private_key, config.password)
if not public_key or not private_key:
    kloader.write_public_key_to_file(config.public_key_path, cryptor.public_key)
listener = sockets.SocketListener()

address_storage = storage.AddressStorage(config.known_ips_file_path)
known_ips = address_storage.load_addresses()
key_storage = storage.KeyStorage(config.known_keys, kloader)
uuid_storage = storage.UUIDStorage(1000)


def on_connect(sender: sockets.SocketSender) -> Callable[[sockets.SocketReader, threading.Event], None]:
    def wrapper(socket_reader: sockets.SocketReader, kill_threads: threading.Event) -> None:
        while not kill_threads.is_set():
            msg = socket_reader.poll()

            if not msg:
                break
            
            message = models.MessageFromDictMapper(json.loads(msg))

            if uuid_storage.have(message.uuid):
                continue

            uuid_storage.add(message.uuid)
            for ip, port in known_ips:
                sender.send(ip, port, json.loads(msg))

            user: str = 'User(no pub key)'
            if message.signature:
                if cryptor.verify_signature(message.signature):
                    key_storage.try_add_key(message.signature.public_key)
                    user = str(models.User(message.signature.public_key, kloader))
            
            if message.type == 'private':
                try:
                    text = cryptor.decrypt(message.text)
                    print(f'{user}[{message.type}]: {text}')
                except ValueError:
                    ...
            else:
                print(f'{user}[{message.type}]: {message.text.decode()}')


    def wrapper2(socket_reader: sockets.SocketReader, kill_threads: threading.Event) -> None:
        try:
            wrapper(socket_reader, kill_threads)
        except KeyboardInterrupt:
            print('\nExiting...')

    return wrapper2


def main() -> None:
    sender = sockets.SocketSender()
    listener.listen_on(config.ip, config.port, on_connect(sender))


if __name__ == '__main__':
    main()
