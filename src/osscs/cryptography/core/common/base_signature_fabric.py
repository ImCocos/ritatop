from typing import Protocol

from osscs.cryptography.core.common import BaseDecryptor, BaseEncryptor
from osscs.cryptography.models.signature import Signature


class BaseSignatureFabric(Protocol):
    def __init__(
        self,
        encryptor: BaseEncryptor,
        decryptor: BaseDecryptor
    ) -> None:
        raise NotImplementedError

    def __call__(self) -> Signature:
        raise NotImplementedError
