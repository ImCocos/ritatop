```python
import threading
# not required; used only for no file-splitting; better use client.py and server.py splitting

from osscs.backend.client import MessageSender
# to send messages
from osscs.backend.server import MessageListener
# to receive messages
from osscs.backend.core import SocketSender, SocketListener
# to send and read from sockets
from osscs.backend.storage import IPv4Address
# IPv4 address to send and receive from
from osscs.backend.storage.common import BaseAddress
# for annotations
from osscs.backend.models import Message, MessagePreparer, User
# To create, encode, sign messages
from osscs.cryptography.core import Encryptor, KeyLoader, Decryptor, SignatureVerifier
# to encode, decode, load data; to create and verify signatures


password = '12345'

addr = IPv4Address('127.0.0.1', 12012)

key_loader = KeyLoader()

decryptor = Decryptor(key_loader, key_loader.generate_private_key(), password)
encryptor = Encryptor(key_loader, decryptor.public_key())

signature_verifier = SignatureVerifier(encryptor, key_loader)

message_preparer = MessagePreparer(encryptor, decryptor)
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