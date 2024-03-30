from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils

from .decryptor import Decryptor
from .encryptor import Encryptor
from osscs.cryptography import models


class SignatureFabric:
    def __init__(self, encryptor: Encryptor, decryptor: Decryptor) -> None:
        self.encryptor = encryptor
        self.decryptor = decryptor

    def __call__(self) -> models.Signature:
        chosen_hash = hashes.SHA256()
        hasher = hashes.Hash(chosen_hash)
        signature_data = hasher.finalize()

        signature = self.decryptor.private_key.sign(
            signature_data,
            padding=self.encryptor.signature_padding,
            algorithm=utils.Prehashed(chosen_hash)
        )

        return models.Signature(
            self.encryptor.key_loader.get_bytes_public_key(self.encryptor.public_key),
            signature,
            signature_data
        )
