import os

from ..config import Config
from .osscs_sockets import Client
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
client = Client()

with open(config.known_ips_file_path, 'r') as file:
    known_ips = [
        (address.split(':')[0], int(address.split(':')[1]))
        for address in file.read().splitlines()
        if address
    ]

def main() -> None:
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
        
        for ip, port in known_ips:
            client.resend(message.dict(), ip, port)


if __name__ == '__main__':
    try:
        main()
    except BaseException as e:
        print(e)
        ...
