import json
import socket
import threading
from typing import Any, Callable, Self


class Server:
    def __init__(self, ip, port, max_connections_count: int = 10) -> None:
        self.ip = ip
        self.port = port

        self.max_connections_count = max_connections_count

        self.sock = socket.socket()
        # self.sock.settimeout(3)

        self.connections: list[socket.socket] = []
    
    def on_msg_recieve(self, foo: Callable[[dict], None]) -> None:
        def decorator(self: Self, connection: socket.socket) -> None:
            try:
                while True:
                    try:
                        msg = connection.recv(2048)
                    except (KeyboardInterrupt, OSError):
                        break
                    if len(msg) == 0:
                        break
                    dict_msg = json.loads(msg)
                    foo(dict_msg)
            except BaseException:
                self.connections.remove(connection)
        self.on_connect = decorator
            
    def bind(self) -> None:
        self.sock.bind((self.ip, self.port))
        self.sock.listen(self.max_connections_count)
    
    def listen(self) -> None:
        self.bind()
        try:
            while (len(self.connections) < self.max_connections_count):
                connection, (connection_host, connection_port) = self.sock.accept()
                threading.Thread(target=self.on_connect, args=[self, connection]).start()
                self.connections.append(connection)
        except BaseException:
            self.sock.close()
    
    def resend(self, msg: dict[str, Any], ip, port) -> None:
        if self.sock.connect_ex((ip, port)) == 0:
            self.sock.send(json.dumps(msg).encode())
