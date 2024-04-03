import socket

from osscs.backend.core.common import BaseReader
from osscs.backend.storage import IPv4Address
from osscs.backend.storage.common import BaseAddress


class SocketReader(BaseReader):
    '''
    Реализация базового читателя информации.
    Работает с сокетами.
    '''
    def __init__(self, socket: socket.socket) -> None:
        self.socket = socket
        
    def poll(self) -> tuple[bytes, BaseAddress] | tuple[None, None]:
        while True:
            msg, peer_address = self.socket.recvfrom(2048)
            if len(msg) == 0:
                break
            
            if len(peer_address) != 2:
                raise NotImplementedError

            return msg, IPv4Address(*peer_address)
        return None, None
