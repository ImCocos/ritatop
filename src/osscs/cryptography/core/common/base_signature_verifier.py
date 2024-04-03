from typing import Protocol

from osscs.cryptography.core.common.base_encryptor import BaseEncryptor
from osscs.cryptography.models.signature import Signature


class BaseSignatureVerifier(Protocol):
    def __init__(
        self,
        encryptor: BaseEncryptor
    ) -> None:
        raise NotImplementedError
    
    def __call__(self, signature: Signature) -> bool:
        raise NotImplementedError
