from abc import ABC, abstractmethod

from osscs.backend.models import Message
from osscs.backend.models.common import BaseUser
from osscs.cryptography.core.common import BaseEncryptor, BaseDecryptor


class BaseMessagePreparer(ABC):
    '''
    Базовый класс сообщения.
    Можно использовать для аннотаций.
    '''
    @abstractmethod
    def __init__(self, encryptor: BaseEncryptor, decryptor: BaseDecryptor) -> None:...

    @abstractmethod
    def sign(self, message: Message) -> None:...

    @abstractmethod
    def encrypt(self, message: Message, adresat: BaseUser) -> None:...
