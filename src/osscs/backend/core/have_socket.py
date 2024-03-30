import socket as sock


class HaveSocket:
    socket: sock.socket

    def create_socket(self) -> None:
        if not hasattr(self, 'socket'):
            self.socket = sock.socket(sock.AF_INET, sock.SOCK_DGRAM)
        
    def shutdown_socket(self) -> None:
        if hasattr(self, 'socket'):
            self.socket.shutdown(1)
    
    def close_socket(self) -> None:
        if hasattr(self, 'socket'):
            self.socket.close()
