import base64
import hashlib

from cryptography.hazmat.primitives.asymmetric import rsa

from .common import AbstarctRSAKeyLoader


class KeyHasherSHA1:
    def __init__(self, key_loader: AbstarctRSAKeyLoader) -> None:
        self.key_loader = key_loader
    def string_hash_public_key(self, key: bytes | rsa.RSAPublicKey) -> str:
        if isinstance(key, rsa.RSAPublicKey):
            return base64.b64encode(hashlib.sha1(self.key_loader.get_bytes_public_key(key)).digest()).decode().replace('/', '')
        elif isinstance(key, bytes):
            return base64.b64encode(hashlib.sha1(key).digest()).decode().replace('/', '')
        else:
            raise NotImplemented
