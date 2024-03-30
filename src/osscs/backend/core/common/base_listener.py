from abc import ABC, abstractmethod
from typing import Callable

from osscs.backend import storage


class BaseListener(ABC):
    @abstractmethod
    def listen_on(
        self,
        address: storage.BaseAddress,
        on_message: Callable[[dict, tuple[str, int]], None]
    ) -> None:...

    @abstractmethod
    def address_is_supported(self, address: storage.BaseAddress) -> bool:...
