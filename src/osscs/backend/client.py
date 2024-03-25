import os

from . import SocketSender
from . import KeyStorage
from . import User
from . import Message
from . import AddressStorage
from ..config import Config
from ..cryptography import Cryptor
from ..cryptography import KeyLoader


config = Config()
kloader = KeyLoader()
cryptor = Cryptor(
    config.password,
    kloader.get_rsa_private_key_from_file(config.private_key_path, config.password),
    kloader.get_rsa_public_key_from_file(config.public_key_path)
)
sender = SocketSender()
address_storage = AddressStorage(config.known_ips_file_path)
known_ips = address_storage.load_addresses()
key_storage = KeyStorage(config.known_keys)

def send() -> None:
    while True:
        users = []
        msg = input('Type your message(<=190s): ')
        sign = input('Sign message?[y/N]:').lower() not in ('n', 'no')
        if input('Type of message[private/public]: ') == 'private':
            print('\n' + '-'*os.get_terminal_size()[0] + '\n')
            for idx, key in enumerate(key_storage.load_keys()):
                user = User(key)
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
