from osscs.backend.client import (
    MessageSender
    # Отправитель сообщений. Используется для отправки сообщений.
)
from osscs.backend.client.common import (
    BaseMessageSender
    # Тип отправителя сообщений. Использутеся для аннотаций.
)

from osscs.backend.core import (
    SocketSender,
    # Отправитель байтовой информации для работы с сокетами.
    SocketListener,
    # Слушатель байтовой информации для работы с сокетами.
    SocketReader
    # Читатель байтовой информации для работы с сокетами.
)
from osscs.backend.core.common import (
    BaseSender,
    # Тип отправителя байтовой информации. Использутеся для аннотаций.
    BaseListener,
    # Тип слушателя байтовой информации. Использутеся для аннотаций.
    BaseReader
    # Тип читателя байтовой информации. Использутеся для аннотаций.
)

from osscs.backend.models import (
    Message,
    # Pydantic-модель сообщения. Может использоваться для аннотаций.
    User,
    # Модель юзера. Может использоваться для аннотаций.
    MessagePreparer
    # Препэйрер сообщений. Используется для подписи, шифрования сообщений.
)
from osscs.backend.models.common import (
    BaseMessagePreparer,
    # Тип препэйрера сообщений. Использутеся для аннотаций.
    BaseUser
    # Тип модели юзера. Использутеся для аннотаций.
)

from osscs.backend.server import (
    MessageListener
    # Слушатель сообщений. Используется напрямую.
)
from osscs.backend.server.common import (
    BaseMessageListener
    # Тип слушателя сообщений. Использутеся для аннотаций.
)

from osscs.backend.storage import (
    KeyStorage,
    # Хранилище ключей(юзеров). Хранит в файловой системе. Используется для CRD(Create Read Delete(еще не реализованно)) ключей(юзеров).
    UUIDStorage,
    # Хранилище юидов. Хранит в ОЗУ. Используется для CRD(Create Read Delete(еще не реализованно)) юидов.
    AddressStorage,
    # Хранилище адресов. Хранит в файловой системе. Используется для CRD(Create Read Delete(еще не реализованно)) адресов.
    IPv4Address,
    # IPv4-адрес
    IPv6Address
    # IPv6-адрес(еще не поддерживается)
)
from osscs.backend.storage.common import (
    BaseAdressStorage,
    # Тип хранилища. Использутеся для аннотаций.
    BaseAddress
    # Тип адреса. Использутеся для аннотаций.
)

from osscs.cryptography.core import (
    Encryptor,
    # Шифровщик байтовой информации. Используется для шифрования байтовой информации.
    Decryptor,
    # Деифровщик байтовой информации. Используется для дешифрования байтовой информации.
    KeyLoader,
    # Сериализатор ключей. Используется для [де]сериализации ключей.
    SignatureFabric,
    # Фабрика подписей. Используется для создания подписей.
    SignatureVerifier
    # Верификатор подписей. Используется для верификации подписи.
)
from osscs.cryptography.core.common import (
    BaseEncryptor,
    # Тип шифровщика байтовой информации. Использутеся для аннотаций.
    BaseDecryptor,
    # Тип дешифровщика байтовой информации. Использутеся для аннотаций.
    BaseRSAKeyLoader,
    # Тип сериализатора ключей. Использутеся для аннотаций.
    BaseSignatureFabric,
    # Тип фабрики подписей. Использутеся для аннотаций.
    BaseSignatureVerifier
    # Тип верификатора подписей. Использутеся для аннотаций.
)