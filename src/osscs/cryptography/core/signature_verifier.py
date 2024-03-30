from cryptography import exceptions
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives.asymmetric import padding

from osscs.cryptography.core.common import BaseSignatureVerifier
from osscs.cryptography.core.common.base_encryptor import BaseEncryptor
from osscs.cryptography.core.common.base_rsa_keys import BaseRSAPublicKey
from osscs.cryptography.models.signature import Signature


class SignatureVerifier(BaseSignatureVerifier):
    def __init__(self, encryptor: BaseEncryptor) -> None:
        self.encryptor = encryptor

        self.signature_padding = padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        )

    def __call__(self, signature: Signature) -> bool:
        try:
            public_key = self.encryptor.key_loader.get_rsa_public_key(signature.public_key)
            if not isinstance(public_key, BaseRSAPublicKey):
                raise ValueError(f'Wrong key')
            public_key.verify(
                signature.signature,
                signature.signature_data,
                padding=self.signature_padding,
                algorithm=utils.Prehashed(hashes.SHA256())
            )
            return True
        except exceptions.InvalidSignature:
            return False
