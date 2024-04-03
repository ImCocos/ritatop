import base64
from uuid import UUID, uuid1

from pydantic import BaseModel, Field, field_serializer, field_validator

from osscs.cryptography.models import Signature


class Message(BaseModel):
    uuid: UUID = Field(default_factory=uuid1)
    text: bytes
    signature: None | Signature = Field(default=None)
    
    @field_serializer('text')
    def serialize_text(self, text: bytes) -> bytes:
        return base64.b64encode(text)
    
    @field_validator('text', check_fields=False)
    def validate_text(cls, text: bytes) -> bytes:
        try:
            return base64.b64decode(text, validate=True)
        except ValueError:
            return text
