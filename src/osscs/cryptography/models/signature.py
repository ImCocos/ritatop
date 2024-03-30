from dataclasses import dataclass


@dataclass
class Signature:
    public_key: bytes
    signature: bytes
    signature_data: bytes
