from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding

from ...cryptography import core


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

    def __init__(self, public_key: rsa.RSAPublicKey | bytes, key_loader: core.AbstarctRSAKeyLoader) -> None:
        self.kloader = key_loader
        self.public_key = public_key if isinstance(public_key, rsa.RSAPublicKey) else self.kloader.get_rsa_public_key(public_key)
        self.padding = padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
