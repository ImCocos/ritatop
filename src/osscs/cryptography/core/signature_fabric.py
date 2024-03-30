from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives.asymmetric import padding

from osscs.cryptography.core.common import BaseEncryptor, BaseDecryptor, BaseSignatureFabric
from osscs.cryptography.models import Signature


class SignatureFabric(BaseSignatureFabric):
    def __init__(self, encryptor: BaseEncryptor, decryptor: BaseDecryptor) -> None:
        self.encryptor = encryptor
        self.decryptor = decryptor
    
        self.signature_padding = padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        )

    def __call__(self) -> Signature:
        chosen_hash = hashes.SHA256()
        hasher = hashes.Hash(chosen_hash)
        signature_data = hasher.finalize()

        signature = self.decryptor.private_key.sign( # type: ignore
            signature_data,
            padding=self.signature_padding,
            algorithm=utils.Prehashed(chosen_hash)
        )

        return Signature(
            self.encryptor.get_bytes_public_key(),
            signature,
            signature_data
        )
