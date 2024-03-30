from abc import ABC, abstractmethod

from osscs.backend import storage


class BaseSender(ABC):
    @abstractmethod
    def send(self, address: storage.BaseAddress, msg: dict[str, str]) -> None:...
    
    @abstractmethod
    def address_is_supported(self, address: storage.BaseAddress) -> bool:...
