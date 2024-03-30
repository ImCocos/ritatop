from abc import ABC, abstractmethod

from osscs.backend.storage.common import BaseAddress


class BaseReader(ABC):
    @abstractmethod
    def poll(self) -> tuple[bytes, BaseAddress] | tuple[None, None]:...
