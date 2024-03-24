from cryptography import exceptions
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives.asymmetric import padding

from . import models
from . import key_loader


class Cryptor:
    def __str__(self) -> str:
        return f'Cryptor({self.get_bytes_public_key().decode().splitlines()[-2][-10:]})'

    def get_bytes_public_key(self) -> bytes:
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.PKCS1,
        )
    
    def get_bytes_private_key(self) -> bytes:
        return self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(self.password.encode())
        )

    def __init__(
            self,
            password: str,
            private_key: None | rsa.RSAPrivateKey = None,
            public_key: None | rsa.RSAPublicKey = None
    ) -> None:
        self.password = password

        self.private_key = private_key if private_key else rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.public_key = public_key if public_key and private_key else self.private_key.public_key()

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

    def get_signature(self) -> models.Signature:
        chosen_hash = hashes.SHA256()
        hasher = hashes.Hash(chosen_hash)
        signature_data = hasher.finalize()

        signature = self.private_key.sign(
            signature_data,
            padding=self.signature_padding,
            algorithm=utils.Prehashed(chosen_hash)
        )

        return models.Signature(
            self.get_bytes_public_key(),
            signature,
            signature_data
        )

    def verify_signature(self, signature: models.Signature) -> bool:
        kloader = key_loader.KeyLoader()
        try:
            public_key = kloader.get_rsa_public_key(signature.public_key)
            if not isinstance(public_key, rsa.RSAPublicKey):
                raise ValueError(f'Wrong key')
            public_key.verify(
                signature.signature,
                signature.signature_data,
                padding=self.signature_padding,
                algorithm=utils.Prehashed(hashes.SHA256())
            )
            return True
        except exceptions.InvalidSignature:
            return False
