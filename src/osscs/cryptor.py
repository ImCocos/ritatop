from cryptography import exceptions
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import utils

from osscs import models


class Cryptor:
    def __str__(self) -> str:
        return f'Cryptor({self.get_bytes_public_key().decode().splitlines()[-2][-10:]})'

    def get_bytes_public_key(self) -> bytes:
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.PKCS1,
        )

    def load_public_key_from_file(self, file_path: str = '') -> rsa.RSAPublicKey | None:
        try:
            with open(file_path, "rb") as public_key_file:
                public_key = public_key_file.read()
            return self.load_public_key(public_key)
        except (FileNotFoundError, ValueError):
            return None
    
    def write_public_key_to_file(self, file_path: str = '') -> None:
        try:
            with open(file_path, "wb") as public_key_file:
                public_key_file.write(
                    self.public_key.public_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PublicFormat.PKCS1,
                    )
                )
        except (FileNotFoundError, ValueError):
            return None
    
    def load_public_key(self, public_key: bytes) -> rsa.RSAPublicKey:
        return serialization.load_pem_public_key(
                public_key,
            ) # type: ignore
    
    def get_bytes_private_key(self) -> bytes:
        return self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(self.password.encode())
        )

    def load_private_key_from_file(self, file_path: str = '') -> rsa.RSAPrivateKey | None:
        try:
            with open(file_path, "rb") as private_key_file:
                private_key = private_key_file.read()
            return self.load_private_key(private_key)
        except (FileNotFoundError, ValueError):
            return None
    
    def write_private_key_to_file(self, file_path: str = '') -> None:
        try:
            with open(file_path, "wb") as private_key_file:
                private_key_file.write(
                    self.private_key.private_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.PKCS8,
                        encryption_algorithm=serialization.BestAvailableEncryption(self.password.encode())
                    )
                )
        except (FileNotFoundError, ValueError):
            return None

    def load_private_key(self, private_key: bytes) -> rsa.RSAPrivateKey:
        return serialization.load_pem_private_key(
                private_key,
                self.password.encode()
            ) # type: ignore

    def __init__(
            self,
            password: str,
            private_key_path: str,
            public_key_path: str
    ) -> None:
        self.password = password

        loaded_private_key = self.load_private_key_from_file(private_key_path)
        if not loaded_private_key:
            self.private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048
            )
            self.write_private_key_to_file(private_key_path)
        else:
            self.private_key = loaded_private_key

        loaded_public_key = self.load_public_key_from_file(public_key_path)
        if not loaded_public_key or not loaded_private_key:
            self.public_key = self.private_key.public_key()
            self.write_public_key_to_file(public_key_path)
        else:
            self.public_key = loaded_public_key

        self.padding = padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )

    def decrypt(self, string: bytes) -> str:
        return self.private_key.decrypt(
            string,
            self.padding
        ).decode()

    def get_signature(self) -> models.Signature:
        chosen_hash = hashes.SHA256()
        hasher = hashes.Hash(chosen_hash)
        signature_data = hasher.finalize()

        signature = self.private_key.sign(
            signature_data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            utils.Prehashed(chosen_hash)
        )

        return models.Signature(
            self.get_bytes_public_key(),
            signature,
            signature_data
        )

    def verify_signature(self, signature: models.Signature) -> bool:
        try:
            serialization.load_pem_public_key(signature.public_key).verify( # type: ignore
                signature.signature,
                signature.signature_data,
                padding=padding.PSS( # type: ignore
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                algorithm=utils.Prehashed(hashes.SHA256()) # type: ignore
            ) # type: ignore
            return True
        except exceptions.InvalidSignature:
            return False