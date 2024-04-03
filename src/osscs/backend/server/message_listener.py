from typing import Callable

from osscs.backend.models import Message
from osscs.backend.core.common import BaseListener
from osscs.backend.server.common import BaseMessageListener
from osscs.backend.storage.common import BaseAddress


class MessageListener(BaseMessageListener):
    def __init__(self, listener: BaseListener) -> None:
        self.listener = listener
    
    def listen_on(self, address: BaseAddress, on_message: Callable[[Message, BaseAddress], None]) -> None:
        def wrapper(bmessage: bytes, address: BaseAddress) -> None:

            try:
                message = Message.model_validate_json(bmessage)
            except BaseException as e:
                print(e)
                return

            on_message(message, address)

        self.listener.listen_on(
            address,
            wrapper
        )
