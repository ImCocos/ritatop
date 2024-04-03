from typing import Protocol

from osscs.cryptography.core.common.base_key_loader import BaseRSAKeyLoader
from osscs.cryptography.core.common.base_rsa_keys import BaseRSAPublicKey


class BaseKeyHasher(Protocol):
    def __init__(self, key_loader: BaseRSAKeyLoader) -> None:
        raise NotImplementedError
    
    def string_hash_public_key(self, key: bytes | BaseRSAPublicKey) -> str:
        raise NotImplementedError
