import os

from ..config import Config
# from .sockets import Client
from .sockets import SocketSender
from ..cryptography.user import User
from ..cryptography.cryptor import Cryptor
from ..cryptography.message import Message
from ..cryptography.key_loader import KeyLoader


config = Config()
kloader = KeyLoader()
cryptor = Cryptor(
    config.password,
    kloader.get_rsa_private_key_from_file(config.private_key_path, config.password),
    kloader.get_rsa_public_key_from_file(config.public_key_path)
)
sender = SocketSender()

with open(config.known_ips_file_path, 'r') as file:
    known_ips = [
        (address.split(':')[0], int(address.split(':')[1]))
        for address in file.read().splitlines()
        if address
    ]

def send() -> None:
    while True:
        users = []
        msg = input('Type your message(<=190s): ')
        sign = input('Sign message?[y/N]:').lower() not in ('n', 'no')
        if input('Type of message[private/public]: ') == 'private':
            print('\n' + '-'*os.get_terminal_size()[0] + '\n')
            for idx, name in enumerate(os.listdir(config.known_keys)):
                with open(os.path.join(config.known_keys, name), 'rb') as key_file:
                    user = User(kloader.get_rsa_public_key(key_file.read()))
                    users.append(user)
                print(f'{idx}) {user}')
                    
            print('\n' + '-'*os.get_terminal_size()[0] + '\n')
            
            adresat_idx = int(input('Type adresat number: '))
            
            adresat = users[adresat_idx]
        else:
            adresat = None
        
        message = Message(msg, adresat)
        if sign:
            message.sign(cryptor)
        
        sender.send(message.dict())


def main() -> None:
    for ip, port in known_ips:
        sender.connect(ip, port)
    print(*(s.getsockname() for s in sender.conections))

    try:
        send()
    except KeyboardInterrupt:
        print('\nQuiting...')


if __name__ == '__main__':
    main()
