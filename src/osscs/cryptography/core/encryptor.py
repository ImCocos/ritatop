from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

from osscs.cryptography.core.common import BaseEncryptor, BaseRSAKeyLoader, BaseRSAPublicKey


class Encryptor(BaseEncryptor):
    def __init__(self, key_loader: BaseRSAKeyLoader, public_key: BaseRSAPublicKey) -> None:
        self.key_loader = key_loader
        self.public_key = public_key
        self.padding = padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )

    def __str__(self) -> str:
        return f'User({self.get_10_symbols()})'

    def get_10_symbols(self) -> str:
        return self.get_bytes_public_key().decode().splitlines()[-2][-10:]

    def encrypt(self, string: str) -> bytes:
        return self.public_key.encrypt(
            string.encode(),
            self.padding
        )
    
    def get_bytes_public_key(self) -> bytes:
        return self.key_loader.get_bytes_public_key(self.public_key)
