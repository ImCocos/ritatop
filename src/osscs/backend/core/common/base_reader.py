from typing import Protocol

from osscs.backend.storage.common import BaseAddress


class BaseReader(Protocol):
    '''
    Базовый класс читателя информации.
    Может использоваться для аннотаций.
    Может использоваться для isinstance.
    '''
    def poll(self) -> tuple[bytes, BaseAddress] | tuple[None, None]:
        raise NotImplementedError
