from typing import Protocol

from osscs.backend.storage.common import BaseAddress


class BaseSender(Protocol):
    '''
    Базовый класс отправителя информации.
    Может использоваться для аннотаций.
    Может использоваться для isinstance.
    '''
    def send(self, address: BaseAddress, message: bytes) -> None:
        raise NotImplementedError
    
    def address_is_supported(self, address: BaseAddress) -> bool:
        raise NotImplementedError
