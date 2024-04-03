from abc import ABC, abstractmethod

from osscs.backend.models import Message
from osscs.cryptography.core.common import BaseEncryptor
from osscs.cryptography.core import SignatureFabric


class BaseMessagePreparer(ABC):
    '''
    Базовый класс сообщения.
    Можно использовать для аннотаций.
    '''
    @abstractmethod
    def sign(self, message: Message, signature_fabric: SignatureFabric) -> None:...

    @abstractmethod
    def encrypt(self, message: Message, encryptor: BaseEncryptor) -> None:...
