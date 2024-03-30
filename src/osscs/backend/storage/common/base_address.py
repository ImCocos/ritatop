from abc import ABC, abstractmethod


class BaseAddress(ABC):
    @abstractmethod
    def data(self) -> str:...

class BaseAdressStorage(ABC):
    @abstractmethod
    def load_addresses(self) -> list[BaseAddress]:...
    
    @abstractmethod
    def try_add_address(self, address: BaseAddress) -> None:...
