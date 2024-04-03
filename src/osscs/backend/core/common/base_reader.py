from abc import ABC, abstractmethod

from osscs.backend.storage.common import BaseAddress


class BaseReader(ABC):
    '''
    Базовый класс читателя информации.
    Может использоваться для аннотаций.
    Может использоваться для isinstance.
    '''
    @abstractmethod
    def poll(self) -> tuple[bytes, BaseAddress] | tuple[None, None]:...
