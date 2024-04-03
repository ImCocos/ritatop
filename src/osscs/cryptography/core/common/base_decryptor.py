from typing import Protocol

from osscs.cryptography.core.common.base_key_loader import BaseRSAKeyLoader
from osscs.cryptography.core.common.base_rsa_keys import BaseRSAPrivateKey, BaseRSAPublicKey


class BaseDecryptor(Protocol):
    def __init__(
        self,
        key_loader: BaseRSAKeyLoader,
        private_key: BaseRSAPrivateKey,
        password: str
    ) -> None:
        raise NotImplementedError
    
    def decrypt(self, data: bytes) -> str:
        raise NotImplementedError

    def public_key(self) -> BaseRSAPublicKey:
        raise NotImplementedError

    def get_bytes_private_key(self) -> bytes:
        raise NotImplementedError
