from osscs.backend.core.common import BaseSender
from osscs.backend.core.have_socket import HaveSocket
from osscs.backend.storage.common import BaseAddress
from osscs.backend.storage import IPv4Address, IPv6Address


TAccessedSocketAddress = IPv4Address | IPv6Address


class SocketSender(HaveSocket, BaseSender):
    def __init__(self) -> None:
        self.create_socket()
    
    def send(self, address: BaseAddress, message: bytes) -> None:
        if not self.address_is_supported(address):
            raise NotImplementedError
        self._send(address, message)

    def _send(self, address: TAccessedSocketAddress, msg: bytes) -> None:
        if isinstance(address, IPv4Address):
            self.socket.sendto(msg, (address.ip, address.port))
            return
        elif isinstance(address, IPv6Address):
            raise NotImplementedError

    def close(self) -> None:
        self.close_socket()
    
    def address_is_supported(self, address: BaseAddress) -> bool:
        return isinstance(address, TAccessedSocketAddress)
