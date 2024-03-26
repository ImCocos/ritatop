import socket
import threading
from typing import Callable

from .address_validator import AddressValidator
from .have_socket import HaveSocket
from .socket_reader import SocketReader


class SocketListener(HaveSocket):
    def __init__(self, max_connections: int = 10) -> None:
        self.max_connections = max_connections
        self.connections: dict[socket.socket, threading.Thread] = {}
        self.kill_threads = threading.Event()

        self.create_socket()

    def bind(self, ip: str, port: int) -> None:
        validate_address = AddressValidator()
        validate_address(ip, port)
        self.socket.bind((ip, port))
        self.socket.listen(self.max_connections)
    
    
    def accept_connection(self, on_connection: Callable[[SocketReader, threading.Event], None]) -> None:
        connection, (_, _) = self.socket.accept()
        thread = threading.Thread(target=on_connection, args=(SocketReader(connection), self.kill_threads))
        self.connections[connection] = thread
        thread.start()
    
    def clean_dead_connectons(self) -> None:
        connections_copy = self.connections.copy()
        for connection in connections_copy:
            if not self.connections[connection].is_alive():
                del self.connections[connection]
    
    def kill_connections(self) -> None:
        connections_copy = self.connections.copy()
        for connection in connections_copy:
            del self.connections[connection]
            connection.close()

    def listen_on(self, ip: str, port: int, on_connection: Callable[[SocketReader, threading.Event], None]) -> None:
        self.bind(ip, port)
        
        try:        
            while True:
                self.clean_dead_connectons()
                if len(self.connections) < self.max_connections:
                    self.accept_connection(on_connection)
        except KeyboardInterrupt:
            print('\nClosing server...')
            self.kill_connections()
            self.kill_threads.set()
            self.shutdown_socket()
            self.close_socket()
            print('Connections killed, socket closed')
