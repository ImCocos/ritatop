import json
from osscs import models
from osscs.user import User
from osscs.message import Message
from osscs.cryptor import Cryptor


def sep() -> None:
    print()
    print('-'*10 + '###' + '-'*10)
    print()


cryptor1 = Cryptor(
    'Cool pass1',
    private_key_path='data/rsa/key1.rsa',
    public_key_path='data/rsa/key1.rsa.pub'
)
print(f'cryptor1 - {cryptor1}')
cryptor2 = Cryptor(
    'Cool pass2',
    private_key_path='data/rsa/key2.rsa',
    public_key_path='data/rsa/key2.rsa.pub'
)
print(f'cryptor2 - {cryptor2}')
cryptor3 = Cryptor(
    'Cool pass3',
    private_key_path='data/rsa/key3.rsa',
    public_key_path='data/rsa/key3.rsa.pub'
)
print(f'cryptor3 - {cryptor3}')

cryptors = (
    cryptor1,
    cryptor2,
    cryptor3,
)

sep()

msg = Message(
    'Hello world!'*1000,
    adresat=User(cryptor2.get_bytes_public_key()),
)
msg.sign(cryptor1)
print(msg)
msg_dict = msg.dict()
dumped_msg = json.dumps(msg_dict).encode()
print(dumped_msg)

sep()

message = models.Message(json.loads(dumped_msg))
print(message)
if message.signature:
    user = User(message.signature.public_key)
    print(f'Signature of {user} validity: {cryptors[0].verify_signature(message.signature)}')

sep()

for cryptor in cryptors:
    if message.type == 'private':
        try:
            print(f'{cryptor} tries to decode test_data from {message}')
            test_data = cryptor.decrypt(message.test_data)
            print(f'{cryptor} decoded test_data from {message}; test_data: {test_data}')
            text = cryptor.decrypt(message.text)
            print(f'{cryptor} decoded text from {message}; text: {text}')
        except ValueError:
            print(f'{cryptor} failed decryption of {message}')
    else:
        test_data = message.test_data.decode()
        print(f'{cryptor} decoded test_data from {message}; data: {test_data}')
        text = message.text.decode()
        print(f'{cryptor} decoded text from {message}; text: {text}')
    print()
