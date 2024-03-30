import base64
import hashlib

from .common import BaseRSAKeyLoader, BaseKeyHasher, BaseRSAPublicKey


class KeyHasherSHA1(BaseKeyHasher):
    def __init__(self, key_loader: BaseRSAKeyLoader) -> None:
        self.key_loader = key_loader

    def string_hash_public_key(self, key: bytes | BaseRSAPublicKey) -> str:
        if isinstance(key, BaseRSAPublicKey):
            return base64.b64encode(hashlib.sha1(self.key_loader.get_bytes_public_key(key)).digest()).decode().replace('/', '')
        elif isinstance(key, bytes):
            return base64.b64encode(hashlib.sha1(key).digest()).decode().replace('/', '')
        else:
            raise NotImplementedError
