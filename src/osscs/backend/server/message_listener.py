from typing import Callable
from osscs.backend.core.common.base_listener import BaseListener
from osscs.backend.models.message_from_dict_mapper import MessageFromDictMapper
from osscs.backend.server.common import BaseMessageListener
from osscs.backend.storage.common.base_address import BaseAddress


class MessageListener(BaseMessageListener):
    def __init__(self, listener: BaseListener) -> None:
        self.listener = listener
    
    def listen_on(self, address: BaseAddress, on_message: Callable[[MessageFromDictMapper, BaseAddress], None]) -> None:
        self.listener.listen_on(
            address,
            on_message
        )
