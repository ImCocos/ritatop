import uuid
import base64

from .mode import PrivateMode, PublicMode
from .user import User
from ...cryptography import core
from ...cryptography import models


class Message:
    def __str__(self) -> str:
        return f'Message(adresat={self.adresat}, mode={self.type}, signature={self.signature})'

    def __init__(self, text: str, adresat: User | None = None) -> None:
        self.text = text[:190]
        self.adresat = adresat
        self.type = PrivateMode() if self.adresat else PublicMode()
        self.signature: None | models.Signature = None

    def sign(self, cryptor: core.Cryptor) -> None:
        self.signature = cryptor.get_signature()
    
    def dict(self) -> dict[str, str | dict[str, str]]:
        self.dict_data: dict[str, str | dict[str, str]]
        self.dict_data = {
            'uuid': base64.b64encode(str(uuid.uuid1()).encode()).decode(),
            'type': base64.b64encode(self.type.mode_name.encode()).decode()
        }

        if self.adresat:
            self.dict_data.update({
                'text': base64.b64encode(self.adresat.encrypt(self.text)).decode(),
                'test_data': base64.b64encode(self.adresat.encrypt('test_data')).decode()
            })
        else:
            self.dict_data.update({
                'text': base64.b64encode(self.text.encode()).decode(),
                'test_data': base64.b64encode('test_data'.encode()).decode()
            })

        if self.signature:
            self.dict_data['signature'] = {
                    'signature': base64.b64encode(self.signature.signature).decode(),
                    'signature_data': base64.b64encode(self.signature.signature_data).decode(),
                    'public_key': base64.b64encode(self.signature.public_key).decode()
            }

        return self.dict_data
