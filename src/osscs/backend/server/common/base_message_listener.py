from abc import ABC, abstractmethod
from typing import Callable

from osscs.backend.core.common import BaseListener
from osscs.backend.models.common import BaseMessage
from osscs.backend.storage.common import BaseAddress


class BaseMessageListener(ABC):
    @abstractmethod
    def __init__(
        self,
        listener: BaseListener
    ) -> None:...

    @abstractmethod
    def listen_on(self, address: BaseAddress, on_message: Callable[[BaseMessage, BaseAddress], None]) -> None:...
