from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils

from osscs.cryptography.core.decryptor import Decryptor
from osscs.cryptography.core.encryptor import Encryptor
from osscs.cryptography.models import Signature


class SignatureFabric:
    def __init__(self, encryptor: Encryptor, decryptor: Decryptor) -> None:
        self.encryptor = encryptor
        self.decryptor = decryptor

    def __call__(self) -> Signature:
        chosen_hash = hashes.SHA256()
        hasher = hashes.Hash(chosen_hash)
        signature_data = hasher.finalize()

        signature = self.decryptor.private_key.sign(
            signature_data,
            padding=self.encryptor.signature_padding,
            algorithm=utils.Prehashed(chosen_hash)
        )

        return Signature(
            self.encryptor.key_loader.get_bytes_public_key(self.encryptor.public_key),
            signature,
            signature_data
        )
