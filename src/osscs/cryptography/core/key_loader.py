from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

from osscs.cryptography.core.common import BaseRSAPrivateKey, BaseRSAKeyLoader, BaseRSAPublicKey


class KeyLoader(BaseRSAKeyLoader):
    def get_rsa_public_key_from_file(self, file_path: str) -> BaseRSAPublicKey | None:
        try:
            with open(file_path, "rb") as public_key_file:
                public_key = public_key_file.read()
            return self.get_rsa_public_key(public_key)
        except (FileNotFoundError, ValueError):
            pass

    def get_rsa_private_key_from_file(self, file_path: str, password: str) -> BaseRSAPrivateKey | None:
        try:
            with open(file_path, "rb") as private_key_file:
                private_key = private_key_file.read()
            return self.get_rsa_private_key(private_key, password)
        except (FileNotFoundError, ValueError):
            pass

    def write_public_key_to_file(self, file_path: str, key: bytes | BaseRSAPublicKey) -> None:
        public_key = key if isinstance(key, BaseRSAPublicKey) else self.get_rsa_public_key(key)
        with open(file_path, "wb") as public_key_file:
            public_key_file.write(
                public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.PKCS1,
                )
            )

    def write_private_key_to_file(self, file_path: str, key: bytes | BaseRSAPrivateKey, password: str) -> None:
        private_key = key if isinstance(key, BaseRSAPrivateKey) else self.get_rsa_private_key(key, password)
        with open(file_path, "wb") as public_key_file:
            public_key_file.write(
                private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.BestAvailableEncryption(password.encode())
                )
            )

    def get_rsa_public_key(self, public_key: bytes) -> BaseRSAPublicKey:
        key = serialization.load_pem_public_key(public_key)
        if not isinstance(key, BaseRSAPublicKey):
            raise ValueError(f'Wrong key type: {key.__class__.__name__}')
        return key

    def get_rsa_private_key(self, private_key: bytes, password: str) -> BaseRSAPrivateKey:
        key = serialization.load_pem_private_key(private_key, password.encode())
        if not isinstance(key, BaseRSAPrivateKey):
            raise ValueError(f'Wrong key type: {key.__class__.__name__}')
        return key

    def get_bytes_public_key(self, public_key: BaseRSAPublicKey) -> bytes:
        return public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.PKCS1,
        )
    
    def get_bytes_private_key(self, private_key: BaseRSAPrivateKey, password: str) -> bytes:
        return private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(password.encode())
        )
    
    def generate_private_key(self) -> BaseRSAPrivateKey:
        return rsa.generate_private_key(65537, 2048)
