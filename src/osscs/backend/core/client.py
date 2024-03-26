from .. import sockets
from .. import storage
from .. import models
from ...cryptography import core
from ...config import Config


config = Config()
kloader = core.KeyLoader()
cryptor = core.Cryptor(
    config.password,
    kloader,
    kloader.get_rsa_private_key_from_file(config.private_key_path, config.password),
    kloader.get_rsa_public_key_from_file(config.public_key_path)
)
sender = sockets.SocketSender()
address_storage = storage.AddressStorage(config.known_ips_file_path)
known_ips = address_storage.load_addresses()
key_storage = storage.KeyStorage(config.known_keys, kloader)

def send() -> None:
    while True:
        users = []
        msg = input('Type your message(<=190s): ')
        sign = input('Sign message?[y/N](y):').lower() not in ('n', 'no')
        if input('Type of message[private/public](public): ') == 'private':
            for idx, key in enumerate(key_storage.load_keys()):
                user = models.User(key, kloader)
                users.append(user)
                print(f'{idx}) {user}')
            
            try:
                adresat_idx = int(input('Type adresat number: '))
                adresat = users[adresat_idx]
            except (IndexError, TypeError):
                adresat = None
        else:
            adresat = None
        
        message = models.Message(msg, adresat)
        if sign:
            message.sign(cryptor)
        
        for ip, port in known_ips:
            sender.send(ip, port, message.dict())


def main() -> None:
    try:
        send()
    except KeyboardInterrupt:
        print('\nQuiting...')


if __name__ == '__main__':
    main()
