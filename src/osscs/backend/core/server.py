import json
import threading
from typing import Callable

from osscs.backend import storage
from osscs.backend import models
from osscs.backend import sockets
from osscs.cryptography import core
from osscs.config import Config


def wrapper(
    sender: sockets.SocketSender,
    uuid_storage: storage.UUIDStorage,
    cryptor: core.Cryptor,
    known_ips: list[tuple[str, int]],
    key_storage: storage.KeyStorage,
    key_loader: core.KeyLoader) -> Callable[[dict], None]:

    def on_message(msg_dict: dict) -> None:
        message = models.MessageFromDictMapper(msg_dict)

        if uuid_storage.have(message.uuid):
            return

        uuid_storage.add(message.uuid)
        for ip, port in known_ips:
            sender.send(ip, port, msg_dict)

        user: str = 'User(no pub key)'
        if message.signature:
            if cryptor.verify_signature(message.signature):
                key_storage.try_add_key(message.signature.public_key)
                user = str(models.User(message.signature.public_key, key_loader))
        
        if message.type == 'private':
            try:
                text = cryptor.decrypt(message.text)
                print(f'{user}[{message.type}]: {text}')
                return
            except ValueError:
                return

        print(f'{user}[{message.type}]: {message.text.decode()}')
    
    return on_message


def main() -> None:
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
    sender = sockets.SocketSender()
    
    listener.listen_on(
        config.ip,
        config.port,
        wrapper(
            sender,
            uuid_storage,
            cryptor,
            known_ips,
            key_storage,
            kloader
        )
    )


if __name__ == '__main__':
    main()
