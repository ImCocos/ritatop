import base64
import hashlib

from ..cryptography.key_loader import KeyLoader, rsa


class KeyHasherSHA1:
    def string_hash_public_key(self, key: bytes | rsa.RSAPublicKey) -> str:
        if isinstance(key, rsa.RSAPublicKey):
            key_loader = KeyLoader()
            return base64.b64encode(hashlib.sha1(key_loader.get_bytes_public_key(key)).digest()).decode().replace('/', '')
        elif isinstance(key, bytes):
            return base64.b64encode(hashlib.sha1(key).digest()).decode().replace('/', '')
        else:
            raise NotImplemented
