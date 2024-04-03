from abc import ABC, abstractmethod

from osscs.backend.storage.common import BaseAddress


class BaseSender(ABC):
    '''
    Базовый класс отправителя информации.
    Может использоваться для аннотаций.
    Может использоваться для isinstance.
    '''
    @abstractmethod
    def send(self, address: BaseAddress, message: bytes) -> None:...
    
    @abstractmethod
    def address_is_supported(self, address: BaseAddress) -> bool:...
