from dataclasses import dataclass


@dataclass
class Signature:
    public_key: bytes
    signature: bytes
    signature_data: bytes

    def __str__(self) -> str:
        return f'Signature({self.public_key.decode().splitlines()[-2][-10:]})'
