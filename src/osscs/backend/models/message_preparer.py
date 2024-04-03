from osscs.backend.models.common import BaseMessagePreparer, BaseUser
from osscs.backend.models import Message
from osscs.cryptography.core import SignatureFabric


class MessagePreparer(BaseMessagePreparer):
    def sign(self, message: Message, signature_fabric: SignatureFabric) -> None:
        message.signature = signature_fabric()

    def encrypt(self, message: Message, adresat: BaseUser) -> None:
        message.text = adresat.encrypt(message.text.decode())
