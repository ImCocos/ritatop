from .osscs_sockets import Server
from osscs_cryptography.key_loader import KeyLoader
from osscs_cryptography.user import User
from osscs_cryptography.cryptor import Cryptor
from osscs_cryptography.models.message import Message
from .config import Config


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

server = Server(
    config.ip,
    config.port,
)

with open(config.known_ips_file_path, 'r') as file:
    known_ips = [
        (address.split(':')[0], int(address.split(':')[1]))
        for address in file.read().splitlines()
    ]

print(known_ips)

@server.on_msg_recieve
def on_connect(dict_msg: dict) -> None:
    message = Message(dict_msg)
    
    print(f'Recieve {message}')
    for ip, port in known_ips:
        print(f'Resending to {ip}:{port}')
        server.resend(dict_msg, ip, port)

    if message.signature:
        user = User(message.signature.public_key)
    else:
        user = 'Unknown'
        
    if message.type == 'public':
        text = message.text.decode()
        print(f'{user}[{message.type}]: {text}')
    else:
        try:
            text = cryptor.decrypt(message.text)
            print(f'{user}[{message.type}]: {text}')
        except ValueError:
            ...


def main() -> None:
    server.listen()
    

if __name__ == '__main__':
    try:
        main()
    except BaseException:
        ...
