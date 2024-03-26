import json
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


def on_connect(sender: sockets.SocketSender) -> Callable[[sockets.SocketReader], None]:
    def wrapper(socket_reader: sockets.SocketReader) -> None:
        while True:
            for ip, port in known_ips:
                sender.try_connect(ip, port)

            msg = socket_reader.poll()

            if not msg:
                break
            
            for ip, port in known_ips:
                print(f'Sending msg to {ip}:{port}')
                sender.send(ip, port, json.loads(msg))

            message = models.MessageFromDictMapper(json.loads(msg))
            
            user: str = 'Unknown'
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


    def wrapper2(socket_reader: sockets.SocketReader) -> None:
        try:
            wrapper(socket_reader)
        except KeyboardInterrupt:
            print('\nExiting...')

    return wrapper2


def main() -> None:
    sender = sockets.SocketSender()
    listener.listen_on(config.ip, config.port, on_connect(sender))


if __name__ == '__main__':
    main()
