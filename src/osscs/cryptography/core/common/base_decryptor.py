from abc import ABC, abstractmethod

from .base_key_loader import BaseRSAKeyLoader
from .base_rsa_keys import BaseRSAPrivateKey, BaseRSAPublicKey


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
