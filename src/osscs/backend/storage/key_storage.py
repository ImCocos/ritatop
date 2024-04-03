import os

from osscs.backend.storage.path_validator import PathValidator
from osscs.cryptography.core import KeyHasherSHA1
from osscs.cryptography.core.common import BaseRSAKeyLoader, BaseRSAPublicKey


class KeyStorage:
    def __init__(self, path: str, key_loader: BaseRSAKeyLoader) -> None:
        self.key_loader = key_loader
        path_validator = PathValidator()
        path_validator.validate_directory_path(path)
        self.storage_path = path
        
    def load_keys(self) -> list[BaseRSAPublicKey]:
        keys = []

        for name in os.listdir(self.storage_path):
            keys.append(self.key_loader.get_rsa_public_key_from_file(os.path.join(self.storage_path, name)))

        return keys
    
    def add_key(self, key: bytes | BaseRSAPublicKey) -> None:
        key_hasher = KeyHasherSHA1(self.key_loader)
        file_name = key_hasher.string_hash_public_key(key)
        self.key_loader.write_public_key_to_file(os.path.join(self.storage_path, file_name), key)

    def try_add_key(self, key: bytes | BaseRSAPublicKey) -> None:
        key_hasher = KeyHasherSHA1(self.key_loader)
        if not os.path.exists(
            os.path.join(
                self.storage_path,
                key_hasher.string_hash_public_key(key)
            )
        ):
            self.add_key(key)
