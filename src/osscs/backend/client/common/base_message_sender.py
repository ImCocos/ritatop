from abc import ABC, abstractmethod

from osscs.backend.core.common import BaseSender
from osscs.backend.models import Message
from osscs.backend.storage.common import BaseAddress


class BaseMessageSender(ABC):
    '''
    Базовый класс отправителя сообщений.
    Может использоваться для аннотаций.
    Может использоваться для isinstance.
    '''
    @abstractmethod
    def __init__(
        self,
        sender: BaseSender
    ) -> None:...

    @abstractmethod
    def send(
        self,
        message: Message,
        address: BaseAddress,
    ) -> None:...
