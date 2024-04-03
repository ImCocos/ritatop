from typing import Callable, Protocol

from osscs.backend.storage.common import BaseAddress


class BaseListener(Protocol):
    '''
    Базовый класс слушателя информации.
    Может использоваться для аннотаций.
    Может использоваться для isinstance.
    '''
    def listen_on(
        self,
        address: BaseAddress,
        on_message: Callable[[bytes, BaseAddress], None]
    ) -> None:
        raise NotImplementedError

    def address_is_supported(self, address: BaseAddress) -> bool:
        raise NotImplementedError
