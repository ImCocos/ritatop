from abc import ABC, abstractmethod

from osscs.cryptography.core.common import BaseDecryptor, BaseEncryptor
from osscs.cryptography.models.signature import Signature


class BaseSignatureFabric(ABC):
    @abstractmethod
    def __init__(
        self,
        encryptor: BaseEncryptor,
        decryptor: BaseDecryptor
    ) -> None:...

    @abstractmethod
    def __call__(self) -> Signature:...
