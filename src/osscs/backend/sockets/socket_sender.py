import json

from .have_socket import HaveSocket
from .address_validator import AddressValidator


class SocketSender(HaveSocket):
    def __init__(self) -> None:
        self.create_socket()

    def send(self, ip: str, port: int, msg: dict[str, str | dict[str, str]]) -> None:
        validate_address = AddressValidator()
        validate_address(ip, port)        
        self.socket.sendto(json.dumps(msg).encode(), (ip, port))

    def close(self) -> None:
        self.close_socket()
