import json
import socket
from typing import Any


class Client:
    def __init__(self) -> None:
        self.sock = socket.socket()

    def send(self, msg: dict[str, Any]) -> None:
        self.sock.send(json.dumps(msg).encode())
    
    def connect(self, ip, port) -> None:
        self.sock.connect((ip, port))
    
    def close(self) -> None:
        self.sock.close()
