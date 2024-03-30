from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

from osscs.cryptography.core.common import BaseDecryptor, BaseRSAKeyLoader, BaseRSAPrivateKey, BaseRSAPublicKey


class Decryptor(BaseDecryptor):
    def __init__(self, key_loader: BaseRSAKeyLoader, private_key: BaseRSAPrivateKey, password: str) -> None:
        self.key_loadet = key_loader

        self.private_key = private_key

        self.password = password

        self.padding = padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
        self.signature_padding = padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        )
    
    def decrypt(self, string: bytes) -> str:
        return self.private_key.decrypt(
            string,
            self.padding
        ).decode()
    
    def public_key(self) -> BaseRSAPublicKey:
        return self.private_key.public_key()
