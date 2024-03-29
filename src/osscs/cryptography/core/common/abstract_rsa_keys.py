from abc import ABC, abstractmethod


class AbstarctRSAPublicKey(ABC):
    @abstractmethod
    def encrypt(self, *args, **kwargs) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def public_bytes(self, *args, **kwargs) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def verify(self, *args, **kwargs) -> None:
        raise NotImplementedError


class AbstarctRSAPrivateKey(ABC):
    @abstractmethod
    def decrypt(self, *args, **kwargs) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def public_key(self, *args, **kwargs) -> AbstarctRSAPublicKey:
        raise NotImplementedError

    @abstractmethod
    def sign(self, *args, **kwargs) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def private_bytes(self, *args, **kwargs) -> bytes:
        raise NotImplementedError
