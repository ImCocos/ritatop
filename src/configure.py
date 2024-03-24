import os


os.system("""
mkdir ~/.config/osscs;
mkdir ~/.config/osscs/data;
mkdir ~/.config/osscs/data/rsa;
mkdir ~/.config/osscs/data/rsa/known_keys;
touch ~/.config/osscs/data/ips.txt
echo '
{
    "ip": "",
    "port": 12012,
    "max_connections": 1,
    "private_key_path": "PATH_TO_HOME/.config/osscs/data/rsa/key.rsa",
    "public_key_path": "PATH_TO_HOME/.config/osscs/data/rsa/key.rsa.pub",
    "password": "",
    "known_keys": "PATH_TO_HOME/.config/osscs/data/rsa/known_keys/",
    "recieve_unsigned_messages": true,
    "known_ips_file_path": "PATH_TO_HOME/.config/osscs/data/ips.txt"
}
' > ~/.config/osscs/config.json;
""")
