# from abc import ABC, abstractmethod
from cryptography.hazmat.primitives.asymmetric import rsa


class BaseRSAPublicKey(rsa.RSAPublicKey):
    ...

class BaseRSAPrivateKey(rsa.RSAPrivateKey):
    ...

# class BaseRSAPublicKey(ABC):
#     @abstractmethod
#     def encrypt(self, *args, **kwargs) -> bytes:
#         raise NotImplementedError

#     @abstractmethod
#     def public_bytes(self, *args, **kwargs) -> bytes:
#         raise NotImplementedError

#     @abstractmethod
#     def verify(self, *args, **kwargs) -> None:
#         raise NotImplementedError


# class BaseRSAPrivateKey(ABC):
#     @abstractmethod
#     def decrypt(self, *args, **kwargs) -> bytes:
#         raise NotImplementedError

#     @abstractmethod
#     def public_key(self, *args, **kwargs) -> BaseRSAPublicKey:
#         raise NotImplementedError

#     @abstractmethod
#     def sign(self, *args, **kwargs) -> bytes:
#         raise NotImplementedError

#     @abstractmethod
#     def private_bytes(self, *args, **kwargs) -> bytes:
#         raise NotImplementedError
