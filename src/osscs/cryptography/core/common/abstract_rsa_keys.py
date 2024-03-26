from abc import ABC, abstractmethod


class AbstarctRSAPublicKey(ABC):
    @abstractmethod
    def encrypt(self, *args, **kwargs) -> bytes:
        ...

    @abstractmethod
    def public_bytes(self, *args, **kwargs) -> bytes:
        ...

    @abstractmethod
    def verify(self, *args, **kwargs) -> None:
        ...


class AbstarctRSAPrivateKey(ABC):
    @abstractmethod
    def decrypt(self, *args, **kwargs) -> bytes:
        ...

    @abstractmethod
    def public_key(self, *args, **kwargs) -> AbstarctRSAPublicKey:
        ...

    @abstractmethod
    def sign(self, *args, **kwargs) -> bytes:
        ...

    @abstractmethod
    def private_bytes(self, *args, **kwargs) -> bytes:
        ...
