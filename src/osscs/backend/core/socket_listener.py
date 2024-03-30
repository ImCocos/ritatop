import json
from typing import Callable

from .common import BaseListener
from .have_socket import HaveSocket
from .socket_reader import SocketReader
from osscs.backend import storage
from osscs.backend.storage import common


TAccessedSocketAddress = storage.IPv4Address | storage.IPv6Address


class SocketListener(BaseListener, HaveSocket):
    def __init__(self) -> None:
        self.create_socket()

    def address_is_supported(self, address: common.BaseAddress) -> bool:
        return isinstance(address, TAccessedSocketAddress)

    def _bind(self, address: TAccessedSocketAddress) -> None:
        if isinstance(address, storage.IPv4Address):
            self.socket.bind((address.ip, address.port))
        elif isinstance(address, storage.IPv6Address):
            raise NotImplementedError

    def listen_on(
        self,
        address: TAccessedSocketAddress,
        on_message: Callable[[dict, common.BaseAddress], None]
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
                on_message(dct, peer_address)

        except KeyboardInterrupt:
            print('\nQuiting...')
            self.close_socket()
