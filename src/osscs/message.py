import uuid

from osscs import mode
from osscs import models
from osscs.user import User
from osscs.cryptor import Cryptor


class Message:
    def __str__(self) -> str:
        return f'Message(adresat={self.adresat}, mode={self.type}, signature={self.signature})'

    def __init__(self, text: str, adresat: User | None = None) -> None:
        self.text = text[:190]
        self.adresat = adresat
        self.type = mode.PrivateMode() if self.adresat else mode.PublicMode()
        self.signature: None | models.Signature = None

    def sign(self, cryptor: Cryptor) -> None:
        self.signature = cryptor.get_signature()
    
    def dict(self) -> dict[str, bytes | dict[str, bytes]]:
        self.dict_data: dict[str, bytes | dict[str, bytes]]
        self.dict_data = {
            'uuid': str(uuid.uuid1()).encode(),
            'type': self.type.mode_name.encode()
        }

        if self.adresat:
            self.dict_data.update({
                'text': self.adresat.encrypt(self.text),
                'test_data': self.adresat.encrypt('test_data')
            })
        else:
            self.dict_data.update({
                'text': self.text.encode(),
                'test_data': 'test_data'.encode()
            })

        if self.signature:
            self.dict_data['signature'] = {
                    'signature': self.signature.signature,
                    'signature_data': self.signature.signature_data,
                    'public_key': self.signature.public_key
            }

        return self.dict_data
