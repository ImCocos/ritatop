import os

from cryptography.hazmat.primitives.asymmetric import rsa

from .path_validator import PathValidator
from ...cryptography import KeyLoader
from ...cryptography import KeyHasherSHA1


class KeyStorage:
    def __init__(self, path: str) -> None:
        path_validator = PathValidator()
        path_validator.validate_directory_path(path)
        self.storage_path = path
        
    def load_keys(self) -> list[rsa.RSAPublicKey]:
        keys = []
        key_loader = KeyLoader()

        for name in os.listdir(self.storage_path):
            with open(os.path.join(self.storage_path, name), 'rb') as file:
                key = key_loader.get_rsa_public_key(file.read())
                keys.append(key)

        return keys
    
    def add_key(self, key: bytes | rsa.RSAPublicKey) -> None:
        key_loader = KeyLoader()
        key_hasher = KeyHasherSHA1()
        file_name = key_hasher.string_hash_public_key(key)
        key_loader.write_public_key_to_file(os.path.join(self.storage_path, file_name), key)

    def try_add_key(self, key: bytes | rsa.RSAPublicKey) -> None:
        key_hasher = KeyHasherSHA1()
        if not os.path.exists(
            os.path.join(
                self.storage_path,
                key_hasher.string_hash_public_key(key)
            )
        ):
            self.add_key(key)
