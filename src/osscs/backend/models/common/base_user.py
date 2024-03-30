from abc import ABC, abstractmethod

from osscs.cryptography.core.common import BaseEncryptor


class BaseUser(ABC):
    @abstractmethod
    def __str__(self) -> str:...

    @abstractmethod
    def __init__(
        self,
        encryptor: BaseEncryptor
    ) -> None:...

    @abstractmethod
    def encrypt(self, string: str) -> bytes:...
