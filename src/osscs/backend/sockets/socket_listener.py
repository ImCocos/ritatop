import json
from typing import Callable

from .address_validator import AddressValidator
from .have_socket import HaveSocket
from .socket_reader import SocketReader


class SocketListener(HaveSocket):
    def __init__(self) -> None:
        self.create_socket()

    def bind(self, ip: str, port: int) -> None:
        validate_address = AddressValidator()
        validate_address(ip, port)
        self.socket.bind((ip, port))

    def listen_on(self, ip: str, port: int, on_message: Callable[[dict], None]) -> None:
        self.bind(ip, port)
        socket_reader = SocketReader(self.socket)
        try:        
            while True:
                msg = socket_reader.poll()

                if not msg:
                    continue

                try:
                    dct = json.loads(msg)
                except ValueError:
                    continue
                
                if not isinstance(dct, dict):
                    continue
                
                on_message(dct)

        except KeyboardInterrupt:
            print('\nClosing server...')
            self.close_socket()
            print('Socket closed')
