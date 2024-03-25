from typing import Any


class AddressValidator:
    def __call__(self, ip: Any, port: Any) -> None:
        if not isinstance(ip, str):
            raise ValueError('IP must be instance of str!')
        if not isinstance(port, int):
            raise ValueError('Port must be imstance of int!')
        if not len(ip.split('.')) == 4:
            raise ValueError('Wrong IPv4 format!')
        if not (1 <= port <= 65535):
            raise ValueError('Port must be in range of [1; 65.535]!')
        for part in ip.split('.'):
            try:
                int_part = int(part)
            except TypeError:
                raise ValueError('Wrong IPv4 format!')
            
            if not (0 <= int_part <= 255):
                raise ValueError('Wrong IPv4 format!')
