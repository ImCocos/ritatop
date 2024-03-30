from abc import ABC, abstractmethod

from osscs.backend.storage.common import BaseAddress


class BaseSender(ABC):
    @abstractmethod
    def send(self, address: BaseAddress, message: bytes) -> None:...
    
    @abstractmethod
    def address_is_supported(self, address: BaseAddress) -> bool:...
