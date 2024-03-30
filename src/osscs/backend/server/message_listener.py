import json
from typing import Callable

from osscs.backend.models import MessageFromDictMapper
from osscs.backend.core.common import BaseListener
from osscs.backend.server.common import BaseMessageListener
from osscs.backend.storage.common import BaseAddress


class MessageListener(BaseMessageListener):
    def __init__(self, listener: BaseListener) -> None:
        self.listener = listener
    
    def listen_on(self, address: BaseAddress, on_message: Callable[[MessageFromDictMapper, BaseAddress], None]) -> None:
        def wrapper(bmessage: bytes, address: BaseAddress) -> None:
            try:
                dict_message = json.loads(bmessage)
            except json.decoder.JSONDecodeError:
                return
            
            try:
                message = MessageFromDictMapper(dict_message)
            except BaseException:
                return
            
            on_message(message, address)

        self.listener.listen_on(
            address,
            wrapper
        )
