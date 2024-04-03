from osscs.backend.client.common import BaseMessageSender
from osscs.backend.core.common import BaseSender
from osscs.backend.models import Message
from osscs.backend.storage.common import BaseAddress


class MessageSender(BaseMessageSender):
    '''
    Реализация базового класса отправитля сообщений.
    На данный момент работает только с SocketSender-ами и IPv4-адресами.
    Используется напрямую.
    '''
    def __init__(self, sender: BaseSender) -> None:
        self.sender = sender
    
    def send(self, message: Message, address: BaseAddress) -> None:
        self.sender.send(address, message.model_dump_json().encode())
