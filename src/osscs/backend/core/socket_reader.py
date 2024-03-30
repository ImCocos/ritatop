import socket

from .common import BaseReader
from osscs.backend import storage


class SocketReader(BaseReader):
    def __init__(self, socket: socket.socket) -> None:
        self.socket = socket
        
    def poll(self) -> tuple[bytes, storage.BaseAddress] | tuple[None, None]:
        while True:
            msg, peer_address = self.socket.recvfrom(2048)
            if len(msg) == 0:
                break
            
            if len(peer_address) != 2:
                raise NotImplementedError

            return msg, storage.IPv4Address(*peer_address)
        return None, None
