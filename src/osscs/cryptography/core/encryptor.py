from cryptography import exceptions
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives.asymmetric import padding

from osscs.cryptography.core.common import BaseEncryptor, BaseRSAKeyLoader, BaseRSAPublicKey
from osscs.cryptography.models import Signature


class Encryptor(BaseEncryptor):
    def __init__(self, key_loader: BaseRSAKeyLoader, public_key: BaseRSAPublicKey) -> None:
        self.key_loader = key_loader
        self.public_key = public_key
        self.padding = padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
        self.signature_padding = padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        )

    def __str__(self) -> str:
        return f'User({self.get_10_symbols()})'

    def get_10_symbols(self) -> str:
        return self.key_loader.get_bytes_public_key(self.public_key).decode().splitlines()[-2][-10:]

    def encrypt(self, string: str) -> bytes:
        return self.public_key.encrypt(
            string.encode(),
            self.padding
        )

    def verify_signature(self, signature: Signature) -> bool:
        try:
            public_key = self.key_loader.get_rsa_public_key(signature.public_key)
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
