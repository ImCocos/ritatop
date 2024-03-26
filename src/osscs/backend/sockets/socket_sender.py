import json
import socket

from .address_validator import AddressValidator


class SocketSender:
    def __init__(self) -> None:
        ...

    def try_connect(self, ip: str, port: int) -> socket.socket | None:
        sock = socket.socket()
        sock.settimeout(0.1)
        sig = sock.connect_ex((ip, port))
        if sig == 0:
            return sock

    def send(self, ip: str, port: int, msg: dict[str, str | dict[str, str]]) -> None:
        validate_address = AddressValidator()
        validate_address(ip, port)        
        conn = self.try_connect(ip, port)
        if conn:
            conn.send(json.dumps(msg).encode())
            conn.close()
