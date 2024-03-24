import os

from ..cryptography.user import User
from ..cryptography.cryptor import Cryptor
from ..cryptography.key_loader import KeyLoader
from ..cryptography.models.message import Message
from ..cryptography.hash_utils import KeyHasherSHA1
from ..config import Config
from .osscs_sockets import Server


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
        if address
    ]

print(known_ips)

@server.on_msg_recieve
def on_connect(dict_msg: dict) -> None:
    key_hasher = KeyHasherSHA1()
    message = Message(dict_msg)
    
    for ip, port in known_ips:
        server.resend(dict_msg, ip, port)

    if message.signature:
        user = User(message.signature.public_key)
        key_hash = key_hasher.string_hash_public_key(message.signature.public_key)
        key_path = os.path.join(
            config.known_keys,
            key_hash
        )
        if not os.path.exists(key_path):
            kloader.write_public_key_to_file(
                key_path,
                message.signature.public_key
            )
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
    server.listen(config)
    

if __name__ == '__main__':
    try:
        main()
    except BaseException as e:
        print(e)
        ...
