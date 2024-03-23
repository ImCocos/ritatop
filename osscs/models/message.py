from osscs.models.signature import Signature


class Message:
    def __str__(self) -> str:
        return f'Message({self.type})'

    def __init__(self, data: dict) -> None:
        self.uuid: bytes = data['uuid']
        self.type: str = data['type'].decode()
        self.text: bytes = data['text']
        self.test_data: bytes = data['test_data']
        self.signature: None | Signature = Signature(
            data['signature']['public_key'],
            data['signature']['signature'],
            data['signature']['signature_data']
        ) if data.get('signature') else None
