from abc import ABC, abstractmethod

from osscs.cryptography.core import common


class BaseUser(ABC):
    @abstractmethod
    def __str__(self) -> str:...

    @abstractmethod
    def __init__(
        self,
        encryptor: common.BaseEncryptor
    ) -> None:...

    @abstractmethod
    def encrypt(self, string: str) -> bytes:...
