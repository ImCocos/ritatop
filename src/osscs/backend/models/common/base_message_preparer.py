from typing import Protocol

from osscs.backend.models import Message
from osscs.backend.models.common import BaseUser
from osscs.cryptography.core.common import BaseEncryptor, BaseDecryptor


class BaseMessagePreparer(Protocol):
    '''
    Базовый класс сообщения.
    Можно использовать для аннотаций.
    '''
    def __init__(self, encryptor: BaseEncryptor, decryptor: BaseDecryptor) -> None:
        raise NotImplementedError

    def sign(self, message: Message) -> None:
        raise NotImplementedError

    def encrypt(self, message: Message, adresat: BaseUser) -> None:
        raise NotImplementedError
