from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding


class User:
    def __str__(self) -> str:
        return f'User({self.get_bytes_public_key().decode().splitlines()[-2][-10:]})'

    def get_bytes_public_key(self) -> bytes:
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.PKCS1,
        )

    def encrypt(self, string: str) -> bytes:
        return self.public_key.encrypt(
            string.encode(),
            self.padding
        )

    def load_public_key(self, public_key: bytes) -> rsa.RSAPublicKey:
        return serialization.load_pem_public_key(public_key) # type: ignore

    def __init__(self, public_key: bytes) -> None:
        self.public_key = self.load_public_key(public_key)
        self.padding = padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
