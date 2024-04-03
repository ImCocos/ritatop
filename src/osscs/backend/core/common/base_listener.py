from abc import ABC, abstractmethod
from typing import Callable

from osscs.backend.storage.common import BaseAddress


class BaseListener(ABC):
    '''
    Базовый класс слушателя информации.
    Может использоваться для аннотаций.
    Может использоваться для isinstance.
    '''
    @abstractmethod
    def listen_on(
        self,
        address: BaseAddress,
        on_message: Callable[[bytes, BaseAddress], None]
    ) -> None:...

    @abstractmethod
    def address_is_supported(self, address: BaseAddress) -> bool:...
