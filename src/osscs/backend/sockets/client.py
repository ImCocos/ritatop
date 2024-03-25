import json
import socket
from typing import Any


class Client:
    def __init__(self) -> None:
        self.sock = socket.socket()

    def send(self, msg: dict[str, Any]) -> None:
        self.sock.send(json.dumps(msg).encode())
    
    def resend(self, msg: dict[str, Any], ip, port) -> None:
        if self.connect(ip, port):
            self.send(msg)
            self.close()
            self.sock = socket.socket()
    
    def connect(self, ip, port) -> bool:
        return self.sock.connect_ex((ip, port)) == 0
    
    def close(self) -> None:
        self.sock.close()
