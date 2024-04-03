from typing import Protocol

from osscs.cryptography.core.common.base_key_loader import BaseRSAKeyLoader
from osscs.cryptography.core.common.base_rsa_keys import BaseRSAPublicKey


class BaseEncryptor(Protocol):
    def __init__(
        self,
        key_loader: BaseRSAKeyLoader,
        public_key: BaseRSAPublicKey
    ) -> None:
        raise NotImplementedError
    
    def encrypt(self, string: str) -> bytes:
        raise NotImplementedError
    
    def get_10_symbols(self) -> str:
        raise NotImplementedError

    def get_bytes_public_key(self) -> bytes:
        raise NotImplementedError
