import base64

from ...cryptography import Signature


class InvalidMessage(BaseException):
    ...

class MessageFromDictMapper:
    def __str__(self) -> str:
        return f'Message({self.type})'

    def __init__(self, data: dict) -> None:
        try:
            self.uuid: bytes = base64.b64decode(data['uuid'].encode())
            self.type: str = base64.b64decode(data['type'].encode()).decode()
            self.text: bytes = base64.b64decode(data['text'].encode())
            self.test_data: bytes = base64.b64decode(data['test_data'].encode())
            self.signature: None | Signature = Signature(
                base64.b64decode(data['signature']['public_key'].encode()),
                base64.b64decode(data['signature']['signature'].encode()),
                base64.b64decode(data['signature']['signature_data'].encode())
            ) if data.get('signature') else None
        except BaseException:
            raise InvalidMessage
