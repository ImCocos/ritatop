from typing import Protocol

from osscs.cryptography.core.common import BaseEncryptor


class BaseUser(Protocol):
    def __str__(self) -> str:
        raise NotImplementedError

    def __init__(
        self,
        encryptor: BaseEncryptor
    ) -> None:
        raise NotImplementedError

    def encrypt(self, string: str) -> bytes:
        raise NotImplementedError
