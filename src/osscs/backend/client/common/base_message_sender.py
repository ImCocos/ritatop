from typing import Protocol

from osscs.backend.core.common import BaseSender
from osscs.backend.models import Message
from osscs.backend.storage.common import BaseAddress


class BaseMessageSender(Protocol):
    '''
    Базовый класс отправителя сообщений.
    Может использоваться для аннотаций.
    Может использоваться для isinstance.
    '''
    def __init__(
        self,
        sender: BaseSender
    ) -> None:
        raise NotImplementedError

    def send(
        self,
        message: Message,
        address: BaseAddress,
    ) -> None:
        raise NotImplementedError
