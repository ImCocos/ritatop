from cryptography.hazmat.primitives.asymmetric import rsa

from abc import ABC, abstractmethod


class AbstarctRSAKeyLoader(ABC):
    @abstractmethod    
    def get_rsa_public_key_from_file(self, file_path: str) -> rsa.RSAPublicKey | None:
        ...

    @abstractmethod
    def get_rsa_private_key_from_file(self, file_path: str, password: str) -> rsa.RSAPrivateKey | None:
        ...

    @abstractmethod
    def write_public_key_to_file(self, file_path: str, key: bytes | rsa.RSAPublicKey) -> None:
        ...

    @abstractmethod
    def write_private_key_to_file(self, file_path: str, key: bytes | rsa.RSAPrivateKey, password: str) -> None:
        ...

    @abstractmethod
    def get_rsa_public_key(self, public_key: bytes) -> rsa.RSAPublicKey:
        ...

    @abstractmethod
    def get_rsa_private_key(self, private_key: bytes, password: str) -> rsa.RSAPrivateKey:
        ...

    @abstractmethod
    def get_bytes_public_key(self, public_key: rsa.RSAPublicKey) -> bytes:
        ...
    
    @abstractmethod    
    def get_bytes_private_key(self, private_key: rsa.RSAPrivateKey, password: str) -> bytes:
        ...
