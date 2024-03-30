from .common import BaseUser
from osscs.cryptography.core import common


class User(BaseUser):
    def __init__(self, encryptor: common.BaseEncryptor) -> None:
        self.encryptor = encryptor
    
    def __str__(self) -> str:
        return f'User({self.encryptor.get_10_symbols()})'

    def encrypt(self, string: str) -> bytes:
        return self.encryptor.encrypt(string)
