from typing import TypeAlias
from cryptography.hazmat.primitives.asymmetric import rsa


# class BaseRSAPublicKey(rsa.RSAPublicKey):
    # ...

BaseRSAPublicKey: TypeAlias = rsa.RSAPublicKey

# class BaseRSAPrivateKey(rsa.RSAPrivateKey):
    # ...

BaseRSAPrivateKey: TypeAlias = rsa.RSAPrivateKey
