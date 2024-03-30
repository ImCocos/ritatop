import json
from osscs.backend.client.common import BaseMessageSender
from osscs.backend.core.common import BaseSender
from osscs.backend.models.common import BaseMessage
from osscs.backend.storage.common import BaseAddress


class MessageSender(BaseMessageSender):
    def __init__(self, sender: BaseSender) -> None:
        self.sender = sender
    
    def send(self, message: BaseMessage, address: BaseAddress) -> None:
        self.sender.send(address, json.dumps(message.dict()).encode())
