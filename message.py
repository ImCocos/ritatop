import uuid

from cryptography.hazmat.primitives import serialization

import mode
from cryptor import Cryptor


class Message:
    def __str__(self) -> str:
        return f'Message(text={self.text[:7] + "..."}, cryptor={self.cryptor}, adresat={self.adresat}, mode={self.mode})'

    def __init__(self, text: str, cryptor: Cryptor, adresat: bytes | None = None, mode: mode.BaseMode = mode.PrivateMode()) -> None:
        self.text = text
        self.cryptor: Cryptor = cryptor
        self.mode = mode
        self.adresat = cryptor.load_public_key(adresat) if adresat else None
        self.generate_dict_data()
    
    def generate_dict_data(self) -> None:
        self.dict_data = {
            'uuid': str(uuid.uuid1()),
        }

        if self.mode == mode.PrivateMode():
            self.dict_data.update({
                'text': self.adresat.encrypt(
                    self.text.encode(),
                    self.cryptor.padding
                ),
                'test_data': self.adresat.encrypt(
                   b'test_data',
                    self.cryptor.padding
                )
            }) # type: ignore
        elif self.mode == mode.PublicMode():
            self.dict_data.update({
                'text': self.text
            })

    def sign(self) -> None:
        sign, digest = self.cryptor.get_sign_and_sign_data()
        self.dict_data.update({
            'signature': { # type: ignore
                'sign': sign,
                'sign_data': digest,
                'public_key': self.cryptor.get_bytes_public_key()
            } # type: ignore
        })
    
    def dict(self) -> dict:
        return self.dict_data
