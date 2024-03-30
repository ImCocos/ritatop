import json
from typing import Callable

from osscs.backend.core.common import BaseListener
from osscs.backend.core.have_socket import HaveSocket
from osscs.backend.core.socket_reader import SocketReader
from osscs.backend.models.message_from_dict_mapper import MessageFromDictMapper
from osscs.backend.storage import IPv4Address, IPv6Address
from osscs.backend.storage.common import BaseAddress


TAccessedSocketAddress = IPv4Address | IPv6Address


class SocketListener(BaseListener, HaveSocket):
    def __init__(self) -> None:
        self.create_socket()

    def address_is_supported(self, address: BaseAddress) -> bool:
        return isinstance(address, TAccessedSocketAddress)

    def _bind(self, address: TAccessedSocketAddress) -> None:
        if isinstance(address, IPv4Address):
            self.socket.bind((address.ip, address.port))
        elif isinstance(address, IPv6Address):
            raise NotImplementedError

    def listen_on(
        self,
        address: TAccessedSocketAddress,
        on_message: Callable[[MessageFromDictMapper, BaseAddress], None]
    ) -> None:
        self._bind(address)
        socket_reader = SocketReader(self.socket)
        try:
            while True:
                msg, peer_address = socket_reader.poll()

                if not msg or not peer_address:
                    continue
                
                try:
                    dct = json.loads(msg)
                except json.decoder.JSONDecodeError:
                    continue
                
                if not isinstance(dct, dict):
                    continue
                on_message(MessageFromDictMapper(dct), peer_address)

        except KeyboardInterrupt:
            print('\nQuiting...')
            self.close_socket()
