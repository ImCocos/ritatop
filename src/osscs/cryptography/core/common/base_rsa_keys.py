from cryptography.hazmat.primitives.asymmetric import rsa


class BaseRSAPublicKey(rsa.RSAPublicKey):
    ...

class BaseRSAPrivateKey(rsa.RSAPrivateKey):
    ...
