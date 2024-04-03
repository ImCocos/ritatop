from osscs.backend.models.common import BaseMessagePreparer, BaseUser
from osscs.backend.models import Message
from osscs.cryptography.core import SignatureFabric
from osscs.cryptography.core.common.base_decryptor import BaseDecryptor
from osscs.cryptography.core.common.base_encryptor import BaseEncryptor


class MessagePreparer(BaseMessagePreparer):
    def __init__(self, encryptor: BaseEncryptor, decryptor: BaseDecryptor) -> None:
        self.encryptor = encryptor
        self.decryptor = decryptor

    def sign(self, message: Message) -> None:
        signature_fabric = SignatureFabric(self.encryptor, self.decryptor)
        message.signature = signature_fabric()

    def encrypt(self, message: Message, adresat: BaseUser) -> None:
        message.text = adresat.encrypt(message.text.decode())
