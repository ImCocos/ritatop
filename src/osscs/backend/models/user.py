from osscs.backend.models.common import BaseUser
from osscs.cryptography.core.common import BaseEncryptor


class User(BaseUser):
    def __init__(self, encryptor: BaseEncryptor) -> None:
        self.encryptor = encryptor
    
    def __str__(self) -> str:
        return f'User({self.encryptor.get_10_symbols()})'

    def encrypt(self, string: str) -> bytes:
        return self.encryptor.encrypt(string)
