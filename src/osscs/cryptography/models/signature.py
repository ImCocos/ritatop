import base64

from pydantic import BaseModel, field_serializer, field_validator


class Signature(BaseModel):
    public_key: bytes
    signature: bytes
    signature_data: bytes

    @field_serializer('public_key')
    def serialize_public_key(self, public_key: bytes) -> bytes:
        return base64.b64encode(public_key)

    @field_serializer('signature')
    def serialize_signature(self, signature: bytes) -> bytes:
        return base64.b64encode(signature)

    @field_serializer('signature_data')
    def serialize_signature_data(self, signature_data: bytes) -> bytes:
        return base64.b64encode(signature_data)

    @field_validator('public_key', check_fields=False)
    def validate_public_key(cls, public_key: bytes) -> bytes:
        try:
            return base64.b64decode(public_key, validate=True)
        except ValueError:
            return public_key

    @field_validator('signature', check_fields=False)
    def validate_signature(cls, signature: bytes) -> bytes:
        try:
            return base64.b64decode(signature, validate=True)
        except ValueError:
            return signature

    @field_validator('signature_data', check_fields=False)
    def validate_signature_data(cls, signature_data: bytes) -> bytes:
        try:
            return base64.b64decode(signature_data, validate=True)
        except ValueError:
            return signature_data
