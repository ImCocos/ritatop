import json

from .have_socket import HaveSocket
from .common import BaseSender
from osscs.backend import storage


TAccessedSocketAddress = storage.IPv4Address | storage.IPv6Address


class SocketSender(HaveSocket, BaseSender):
    def __init__(self) -> None:
        self.create_socket()

    def send(self, address: TAccessedSocketAddress, msg: dict[str, str | dict[str, str]]) -> None:
        if not self.address_is_supported(address):
            raise NotImplementedError
        self._send(address, msg)
    
    def _send(self, address: TAccessedSocketAddress, msg: dict[str, str | dict[str, str]]) -> None:
        bdata = json.dumps(msg).encode()

        if isinstance(address, storage.IPv4Address):
            self.socket.sendto(bdata, (address.ip, address.port))
            return
        elif isinstance(address, storage.IPv6Address):
            raise NotImplementedError

    def close(self) -> None:
        self.close_socket()
    
    def address_is_supported(self, address: storage.BaseAddress) -> bool:
        return isinstance(address, TAccessedSocketAddress)
