# OSSCS
This is small messanger base.

It is:
 - open source
 - crypto secure
 - peer to peer
 - end to end encrypted

# Installing

```bash
pip install osscs
```

# Usage

```python
import threading

from osscs.backend.client import MessageSender
from osscs.backend.server import MessageListener
from osscs.backend.core import SocketSender, SocketListener
from osscs.backend.storage import IPv4Address
from osscs.backend.models import Message, MessagePreparer, User
from osscs.cryptography.core import SignatureFabric, Encryptor, KeyLoader, Decryptor, SignatureVerifier
from osscs.types import BaseAddress


password = '12345'

addr = IPv4Address('127.0.0.1', 12012)

key_loader = KeyLoader()

decryptor = Decryptor(key_loader, key_loader.generate_private_key(), password)
encryptor = Encryptor(key_loader, decryptor.public_key())

signature_fabric = SignatureFabric(encryptor, decryptor)
signature_verifier = SignatureVerifier(encryptor, key_loader)


message_preparer = MessagePreparer(encryptor, decryptor, signature_fabric)
message_sender = MessageSender(SocketSender())
message_listener = MessageListener(SocketListener())

def on_message(message: Message, address: BaseAddress) -> None:
    user = 'Anonim'
    if message.signature and signature_verifier(message.signature):
        user = User(Encryptor(key_loader, key_loader.get_rsa_public_key(message.signature.public_key)))
    print(f'{user}[{address.data()}]: {decryptor.decrypt(message.text)}')

threading.Thread(
    target=message_listener.listen_on,
    args=[addr, on_message]
).start()

message = Message(text=b'Hello world')
message_preparer.encrypt(message, User(encryptor))
message_preparer.sign(message)

message_sender.send(
    message,
    addr
)

```

# Documentation in [DOC.py](https://github.com/ImCocos/ritatop/blob/master/DOC.py)