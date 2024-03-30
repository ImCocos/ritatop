from abc import ABC, abstractmethod

from osscs.cryptography.core.common.base_key_loader import BaseRSAKeyLoader
from osscs.cryptography.core.common.base_rsa_keys import BaseRSAPublicKey


class BaseKeyHasher(ABC):
    @abstractmethod
    def __init__(self, key_loader: BaseRSAKeyLoader) -> None:...
    
    @abstractmethod
    def string_hash_public_key(self, key: bytes | BaseRSAPublicKey) -> str:...
