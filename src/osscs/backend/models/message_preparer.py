from osscs.backend.models import Message
from osscs.backend.models.common import BaseMessagePreparer, BaseUser
from osscs.cryptography.core.common import BaseDecryptor, BaseEncryptor, BaseSignatureFabric


class MessagePreparer(BaseMessagePreparer):
    def __init__(self, encryptor: BaseEncryptor, decryptor: BaseDecryptor, signature_fabric: BaseSignatureFabric) -> None:
        self.encryptor = encryptor
        self.decryptor = decryptor
        self.signature_fabric = signature_fabric

    def sign(self, message: Message) -> None:
        message.signature = self.signature_fabric()

    def encrypt(self, message: Message, adresat: BaseUser) -> None:
        message.text = adresat.encrypt(message.text.decode())
