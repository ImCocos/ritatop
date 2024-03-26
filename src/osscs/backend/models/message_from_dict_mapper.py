import base64

from ...cryptography import models


class MessageFromDictMapper:
    def __str__(self) -> str:
        return f'Message({self.type})'

    def __init__(self, data: dict) -> None:
        self.uuid: str = base64.b64decode(data['uuid'].encode()).decode()
        self.type: str = base64.b64decode(data['type'].encode()).decode()
        self.text: bytes = base64.b64decode(data['text'].encode())
        self.test_data: bytes = base64.b64decode(data['test_data'].encode())
        self.signature: None | models.Signature = models.Signature(
            base64.b64decode(data['signature']['public_key'].encode()),
            base64.b64decode(data['signature']['signature'].encode()),
            base64.b64decode(data['signature']['signature_data'].encode())
        ) if data.get('signature') else None
