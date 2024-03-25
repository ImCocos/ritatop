import json
from typing import Callable


from ..cryptography.user import User
from ..cryptography.cryptor import Cryptor
from ..cryptography.key_loader import KeyLoader
from ..cryptography.models.message import Message
from ..cryptography.hash_utils import KeyHasherSHA1
from ..config import Config
from .sockets import SocketListener, SocketSender
from .sockets import SocketReader


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

with open(config.known_ips_file_path, 'r') as file:
    known_ips = [
        (address.split(':')[0], int(address.split(':')[1]))
        for address in file.read().splitlines()
        if address
    ]


def on_connect(sender: SocketSender) -> Callable[[SocketReader], None]:
    def wrapper(socket_reader: SocketReader) -> None:
        while True:
            msg = socket_reader.poll()
            if not msg:
                break
            sender.send(json.loads(msg))
            message = Message(json.loads(msg))
            print(f'{message.text}')

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
