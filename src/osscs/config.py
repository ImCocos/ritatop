import json
import os


class Config:
    def __init__(self, path: str | None = None) -> None:
        self.path = path or os.path.join(os.path.expanduser('~'), '.config/osscs/config.json')
        self.load_config()
    
    def load_config(self) -> None:
        with open(self.path, 'r') as config_file:
            config_dict = json.load(config_file)
            self.ip = config_dict.get('ip')
            self.port = config_dict.get('port')
            self.max_connections = config_dict.get('max_connections')
            self.private_key_path = config_dict.get('private_key_path')
            self.public_key_path = config_dict.get('public_key_path')
            self.password = config_dict.get('password')
            self.known_keys = config_dict.get('known_keys')
            self.recieve_unsigned_messages = config_dict.get('recieve_unsigned_messages')
            self.known_ips_file_path = config_dict.get('known_ips_file_path')
