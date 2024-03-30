from abc import ABC, abstractmethod

from osscs.cryptography.core.common.base_key_loader import BaseRSAKeyLoader
from osscs.cryptography.core.common.base_rsa_keys import BaseRSAPublicKey


class BaseEncryptor(ABC):
    @abstractmethod
    def __init__(
        self,
        key_loader: BaseRSAKeyLoader,
        public_key: BaseRSAPublicKey
    ) -> None:...
    
    @abstractmethod
    def encrypt(self, string: str) -> bytes:...
    
    @abstractmethod
    def get_10_symbols(self) -> str:...

    @abstractmethod
    def get_bytes_public_key(self) -> bytes:...
