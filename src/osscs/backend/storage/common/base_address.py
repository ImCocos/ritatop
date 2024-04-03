from typing import Protocol


class BaseAddress(Protocol):
    def data(self) -> str:
        raise NotImplementedError


class BaseAdressStorage(Protocol):
    def load_addresses(self) -> list[BaseAddress]:
        raise NotImplementedError
    
    def try_add_address(self, address: BaseAddress) -> None:
        raise NotImplementedError
