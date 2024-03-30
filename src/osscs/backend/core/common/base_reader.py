from abc import ABC, abstractmethod

from osscs.backend import storage


class BaseReader(ABC):
    @abstractmethod
    def poll(self) -> tuple[bytes, storage.BaseAddress] | tuple[None, None]:...
