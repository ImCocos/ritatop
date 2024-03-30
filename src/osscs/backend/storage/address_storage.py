from . import common
from .path_validator import PathValidator
from .address_validator import AddressValidator


class IPv4Address(common.BaseAddress):
    def __init__(self, ip: str, port: int) -> None:
        validate_address = AddressValidator()
        validate_address(ip, port)
        self.ip = ip
        self.port = port
    
    def data(self) -> str:
        return f'{self.ip}:{self.port}'


class IPv6Address(common.BaseAddress):
    def __init__(self) -> None:
        raise NotImplementedError


class AddressStorage(common.BaseAdressStorage):
    def __init__(self, path: str) -> None:
        path_validator = PathValidator()
        path_validator.validate_file_path(path)
        self.storage_path = path
    
    def load_addresses(self) -> list[common.BaseAddress]:
        with open(self.storage_path, 'r') as file:
            return [
                IPv4Address(
                    address.split(':')[0],
                    int(address.split(':')[1])
                )
                for address in file.read().splitlines()
                if address
            ]

    def add_address(self, address: common.BaseAddress) -> None:
        with open(self.storage_path, 'a') as file:
            file.write(address.data())

    def try_add_address(self, address: common.BaseAddress) -> None:
        if address.data() not in self.load_addresses():
            self.add_address(address)
