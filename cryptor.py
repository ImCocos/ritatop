import json
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding


class Cryptor:
    def get_string_public_key(self) -> str:
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.PKCS1,
        ).decode()
    
    def load_private_key_from_file(self) -> rsa.RSAPrivateKey | None:
        try:
            with open("key.rsa", "rb") as private_key_file:
                private_key = private_key_file.read()
            return serialization.load_pem_private_key(
                private_key,
                self.password.encode()
            ) # type: ignore
        except (FileNotFoundError, ValueError):
            return None
    
    def write_private_key_to_file(self) -> None:
        with open("key.rsa", "wb") as private_key_file:
            private_key_file.write(
                self.private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.BestAvailableEncryption(self.password.encode())
                )
            )

    def load_public_key_from_file(self) -> rsa.RSAPublicKey | None:
        try:
            with open("key.rsa.pub", "rb") as public_key_file:
                public_key = public_key_file.read()
            return serialization.load_pem_public_key(
                public_key,
            ) # type: ignore
        except (FileNotFoundError, ValueError):
            return None
    
    def write_public_key_to_file(self) -> None:
        with open("key.rsa.pub", "wb") as public_key_file:
            public_key_file.write(
                self.public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.PKCS1,
                )
            )
    
    def get_string_private_key(self) -> str:
        return self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(self.password.encode())
        ).decode()

    def __init__(self, password: str) -> None:
        self.password = password

        loaded_private_key = self.load_private_key_from_file()
        if not loaded_private_key:
            self.private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048
            )
            self.write_private_key_to_file()
        else:
            self.private_key = loaded_private_key

        loaded_public_key = self.load_public_key_from_file()
        if not loaded_public_key:
            self.public_key = self.private_key.public_key()
            self.write_public_key_to_file()
        else:
            self.public_key = loaded_public_key

        self.padding = padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )

        # print(self.get_string_private_key())
        # print(self.get_string_public_key())
    
    def encrypt(self, string: str) -> bytes:
        return self.public_key.encrypt(
            string.encode(),
            self.padding
        )

    def decrypt(self, string: bytes) -> str:
        return self.private_key.decrypt(
            string,
            self.padding
        ).decode()
