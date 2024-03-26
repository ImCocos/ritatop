# ritatop

```
-----BEGIN ENCRYPTED PRIVATE KEY-----
      _ _        _              
 _ __(_) |_ __ _| |_ ___  _ __  
| '__| | __/ _` | __/ _ \| '_ \ 
| |  | | || (_| | || (_) | |_) |
|_|  |_|\__\__,_|\__\___/| .__/ 
                         |_|    
-----END ENCRYPTED PRIVATE KEY-------
```

## Description

This is a small project about p2p connections, sockets, crypthography.

## Advantages

 - open source
 - crypto secure
 - fully decentralized
 - p2p

## Work

 - sockets
 - peer to peer connections
 - rsa keys
 - 1 to all messaging

## Installing

```bash
pip install osscs
python -m osscs.configure
```

### Running

 - Fill the ~/.config/osscs/config.json
 - add few ips to ~/.config/osscs/data/ips.txt(example: 1.1.1.1:12012)
 - `python -m osscs.backend.core.server` (to recieve messages)(in terminal №1)
 - `python -m osscs.backend.core.client` (to send messages)(in terminal №2)
