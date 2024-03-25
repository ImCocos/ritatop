from .path_validator import PathValidator
from ..sockets import AddressValidator


class AddressStorage:
    def __init__(self, path: str) -> None:
        path_validator = PathValidator()
        path_validator.validate_file_path(path)
        self.storage_path = path
    
    def load_addresses(self) -> list[tuple[str, int]]:
        with open(self.storage_path, 'r') as file:
            return [
                (address.split(':')[0], int(address.split(':')[1]))
                for address in file.read().splitlines()
                if address
            ]

    def add_address(self, ip: str, port: int) -> None:
        with open(self.storage_path, 'a') as file:
            file.write(f'{ip}:{port}')

    def try_add_address(self, ip: str, port: int) -> None:
        validate_address = AddressValidator()
        validate_address(ip, port)
        
        if (ip, port) not in self.load_addresses():
            self.add_address(ip, port)
