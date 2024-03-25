import json
import socket

from .address_validator import AddressValidator


class SocketSender:
    def __init__(self) -> None:
        self.conections: list[socket.socket] = []

    def connect(self, ip: str, port: int) -> bool:
        validate_address = AddressValidator()
        validate_address(ip, port)
        sock = socket.socket()
        sig = sock.connect_ex((ip, port))
        if sig == 0:
            self.conections.append(sock)
            return True
        return False

    def send(self, msg: dict[str, str | dict[str, str]]) -> None:
        for sock in self.conections:
            sock.send(json.dumps(msg).encode())
