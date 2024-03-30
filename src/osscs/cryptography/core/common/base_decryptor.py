from abc import ABC, abstractmethod

from osscs.cryptography.core.common.base_key_loader import BaseRSAKeyLoader
from osscs.cryptography.core.common.base_rsa_keys import BaseRSAPrivateKey, BaseRSAPublicKey


class BaseDecryptor(ABC):
    @abstractmethod
    def __init__(
        self,
        key_loader: BaseRSAKeyLoader,
        private_key: BaseRSAPrivateKey,
        password: str
    ) -> None:...
    
    @abstractmethod
    def decrypt(self, data: bytes) -> str:...

    @abstractmethod
    def public_key(self) -> BaseRSAPublicKey:...

    @abstractmethod
    def get_bytes_private_key(self) -> bytes:...
