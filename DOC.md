```python
from osscs.backend.client import MessageSender
'''
Отправщик сообщений, принимает на вход любой сэндер.
Реализует отправку сообщений. Логику для отправки писать НЕ ТРЕБУЕТСЯ.
'''

from osscs.backend.server import MessageListener
'''
Листнер сообщений, принимает на вход любой листнер.
Реализует полл сообщений. Логику для принятие сообщений писать НЕ ТРЕБУЕТСЯ.
'''

from osscs.backend.core import SocketSender, SocketListener
'''
Сокет сэндер и листнер.
Нужны для передачи своего инстанса в вышеописанные классы. 
'''

from osscs.backend.models import Message, MessageFromDictMapper, User
'''
Класс Message - для отправки сообщения.
класс MessageFromDictMapper - для принятия сообщений(исключительно для аннотаций)
Класс User - маппит паблик-ключ на юзера. Используется в качестве адресата для класса Message.
'''

from osscs.backend.storage import IPv4Address
'''
Класс адреса.
'''

from osscs.backend.storage.common import BaseAddress
'''
Класс базового адреса, использовать ИСКЛБЧИТЕЛЬНО для аннотаций.
'''

from osscs.backend.storage import AddressStorage, UUIDStorage, KeyStorage
'''
Класс AddressStorage - для хранения известных адресов.(файл)
Класс UUIDStorage - для хранения uuid-ов сообщений. Использовать ОДИН инстанс на приложение.(ОЗУ)
Класс KeyStorage - для хранения известных юзеров(ключей).(файлы)
'''

from osscs.cryptography.core import Encryptor, Decryptor, KeyLoader
'''
Класс Encryptor - использовать ИСКЛЮЧИТЕЛЬНО для передачи в методы. Можно создавать несколько инстансов, но лучше - один через DI.
Класс Decryptor - использовать ИСКЛЮЧИТЕЛЬНО для передачи в методы. Можно создавать несколько инстансов, но лучше - один через DI.
Класс KeyLoader - использовать ИСКЛЮЧИТЕЛЬНО для передачи в методы И ДЛЯ ИНИЦИАЛИЗАЦИИ вышеописанных методов(т.е. при их инициализации использовать кей-лоадер, для загрузки ключей овнера ПК). Можно создавать несколько инстансов.
'''
```