from typing import Protocol

from osscs.cryptography.core.common.base_rsa_keys import BaseRSAPrivateKey, BaseRSAPublicKey


class BaseRSAKeyLoader(Protocol):
    def get_rsa_public_key_from_file(self, file_path: str) -> BaseRSAPublicKey | None:
        raise NotImplementedError

    def get_rsa_private_key_from_file(self, file_path: str, password: str) -> BaseRSAPrivateKey | None:
        raise NotImplementedError

    def write_public_key_to_file(self, file_path: str, key: bytes | BaseRSAPublicKey) -> None:
        raise NotImplementedError

    def write_private_key_to_file(self, file_path: str, key: bytes | BaseRSAPrivateKey, password: str) -> None:
        raise NotImplementedError

    def get_rsa_public_key(self, public_key: bytes) -> BaseRSAPublicKey:
        raise NotImplementedError

    def get_rsa_private_key(self, private_key: bytes, password: str) -> BaseRSAPrivateKey:
        raise NotImplementedError

    def get_bytes_public_key(self, public_key: BaseRSAPublicKey) -> bytes:
        raise NotImplementedError
    
    def get_bytes_private_key(self, private_key: BaseRSAPrivateKey, password: str) -> bytes:
        raise NotImplementedError
