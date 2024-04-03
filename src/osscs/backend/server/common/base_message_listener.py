from typing import Callable, Protocol

from osscs.backend.core.common import BaseListener
from osscs.backend.models import Message
from osscs.backend.storage.common import BaseAddress


class BaseMessageListener(Protocol):
    def __init__(
        self,
        listener: BaseListener
    ) -> None:
        raise NotImplementedError

    def listen_on(self, address: BaseAddress, on_message: Callable[[Message, BaseAddress], None]) -> None:
        raise NotImplementedError
