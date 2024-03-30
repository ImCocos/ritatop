from abc import ABC, abstractmethod
from typing import Callable

from osscs.backend.models.message_from_dict_mapper import MessageFromDictMapper
from osscs.backend.storage.common import BaseAddress


class BaseListener(ABC):
    @abstractmethod
    def listen_on(
        self,
        address: BaseAddress,
        on_message: Callable[[MessageFromDictMapper, BaseAddress], None]
    ) -> None:...

    @abstractmethod
    def address_is_supported(self, address: BaseAddress) -> bool:...
