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
from osscs.backend.models import Message, MessageFromDictMapper
from osscs.backend.storage import IPv4Address
from osscs.backend.storage.common import BaseAddress


addr = IPv4Address(
    '127.0.0.1',
    12012
)
message_sender = MessageSender(SocketSender())
message_listener = MessageListener(SocketListener())

def on_message(message: MessageFromDictMapper, address: BaseAddress) -> None:
    print(f'{address.data()} - {message.text.decode()}')


threading.Thread(
    target=message_listener.listen_on,
    args=[addr, on_message]
).start()

message_sender.send(
    Message('Hello world'),
    addr
)
```