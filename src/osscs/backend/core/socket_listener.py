from typing import Callable

from osscs.backend.core.common import BaseListener
from osscs.backend.core.have_socket import HaveSocket
from osscs.backend.core import SocketReader
from osscs.backend.storage import IPv4Address, IPv6Address
from osscs.backend.storage.common import BaseAddress


TAccessedSocketAddress = IPv4Address | IPv6Address


class SocketListener(BaseListener, HaveSocket):
    '''
    Реализация базового слушателя информации.
    Слушает сокеты.
    На данный момент работает только с IPv4-адресами.
    '''
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
        on_message: Callable[[bytes, BaseAddress], None]
    ) -> None:
        self._bind(address)
        socket_reader = SocketReader(self.socket)
        try:
            while True:
                msg, peer_address = socket_reader.poll()

                if not msg or not peer_address:
                    continue

                on_message(msg, peer_address)

        except KeyboardInterrupt:
            print('\nQuiting...')
            self.close_socket()
