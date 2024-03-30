from abc import ABC, abstractmethod

from osscs.backend.models.common import BaseUser
from osscs.cryptography.core.signature_fabric import SignatureFabric


class BaseMessage(ABC):
    @abstractmethod
    def __init__(
        self,
        text: str,
        adresat: BaseUser | None,
    ) -> None:...

    @abstractmethod
    def sign(self, signature_fabric: SignatureFabric) -> None:...

    @abstractmethod
    def dict(self) -> dict:...
