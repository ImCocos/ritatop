from .common import BaseRSAKeyLoader, BaseRSAPrivateKey, BaseRSAPublicKey
from .encryptor import Encryptor
from .decryptor import Decryptor


class Cryptor:
    def __str__(self) -> str:
        return f'Cryptor({self.encryptor.get_10_symbols()})'

    def __init__(
            self,
            password: str,
            key_loader: BaseRSAKeyLoader,
            private_key: BaseRSAPrivateKey,
            public_key: BaseRSAPublicKey
    ) -> None:
        self.key_loader = key_loader
        self.password = password

        self.decryptor = Decryptor(
            self.key_loader,
            private_key,
            password
        )
        self.encryptor = Encryptor(
            self.key_loader,
            public_key
        )
