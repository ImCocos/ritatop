from abc import ABC, abstractmethod

from .base_key_loader import BaseRSAKeyLoader
from .base_rsa_keys import BaseRSAPublicKey
from osscs.cryptography.models.signature import Signature


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
    def verify_signature(self, signature: Signature) -> bool:...
    
    @abstractmethod
    def get_10_symbols(self) -> str:...
