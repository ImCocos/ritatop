from abc import ABC, abstractmethod

from osscs.cryptography.core.common.base_encryptor import BaseEncryptor
from osscs.cryptography.models.signature import Signature


class BaseSignatureVerifier(ABC):
    @abstractmethod
    def __init__(
        self,
        encryptor: BaseEncryptor
    ) -> None:...
    
    @abstractmethod
    def __call__(self, signature: Signature) -> bool:...
