import json
from typing import Callable

from . import AddressStorage
from . import KeyStorage
from . import User
from . import SocketReader
from . import MessageFromDictMapper
from . import SocketListener, SocketSender
from ..config import Config
from ..cryptography import Cryptor
from ..cryptography import KeyLoader


config = Config()
kloader = KeyLoader()
private_key = kloader.get_rsa_private_key_from_file(config.private_key_path, config.password)
public_key = kloader.get_rsa_public_key_from_file(config.public_key_path)
cryptor = Cryptor(
    config.password,
    private_key,
    public_key
)
if not private_key:
    kloader.write_private_key_to_file(config.private_key_path, cryptor.private_key, config.password)
if not public_key or not private_key:
    kloader.write_public_key_to_file(config.public_key_path, cryptor.public_key)
listener = SocketListener()

address_storage = AddressStorage(config.known_ips_file_path)
known_ips = address_storage.load_addresses()
key_storage = KeyStorage(config.known_keys)


def on_connect(sender: SocketSender) -> Callable[[SocketReader], None]:
    def wrapper(socket_reader: SocketReader) -> None:
        while True:
            msg = socket_reader.poll()

            if not msg:
                break

            sender.send(json.loads(msg))

            message = MessageFromDictMapper(json.loads(msg))
            
            user: str = 'Unknown'
            if message.signature:
                if cryptor.verify_signature(message.signature):
                    key_storage.try_add_key(message.signature.public_key)
                    user = str(User(message.signature.public_key))
            
            if message.type == 'private':
                try:
                    text = cryptor.decrypt(message.text)
                    print(f'{user}[{message.type}]: {text}')
                except ValueError:
                    ...
            else:
                print(f'{user}[{message.type}]: {message.text.decode()}')


    def wrapper2(socket_reader: SocketReader) -> None:
        try:
            wrapper(socket_reader)
        except KeyboardInterrupt:
            print('\nExiting...')

    return wrapper2


def main() -> None:
    sender = SocketSender()
    for ip, port in known_ips:
        sender.connect(ip, port)
    print(*(s.getsockname() for s in sender.conections))
    listener.listen_on(config.ip, config.port, on_connect(sender))


if __name__ == '__main__':
    main()
