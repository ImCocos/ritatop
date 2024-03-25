import socket


class SocketReader:
    def __init__(self, socket: socket.socket) -> None:
        self.socket = socket
        
    def poll(self) -> bytes | None:
        while True:
            try:
                msg = self.socket.recv(2048)
            except (KeyboardInterrupt, OSError):
                break
            if len(msg) == 0:
                break
            
            return msg
