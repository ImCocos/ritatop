import socket
from typing import Any


class SocketReader:
    def __init__(self, socket: socket.socket) -> None:
        self.socket = socket
        
    def poll(self) -> bytes | None:
        while True:
            msg, _ = self.socket.recvfrom(4096)
            if len(msg) == 0:
                break
            
            return msg
