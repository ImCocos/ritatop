from abc import ABC, abstractmethod

from osscs.backend.storage.common import BaseAddress
from osscs.backend.models.common import BaseMessage


class BaseSender(ABC):
    @abstractmethod
    def send(self, address: BaseAddress, message: BaseMessage) -> None:...
    
    @abstractmethod
    def address_is_supported(self, address: BaseAddress) -> bool:...
