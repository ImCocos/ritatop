import os


w = os.get_terminal_size()[0]
bk = 'BEGIN ENCRYPTED PRIVATE KEY'
lbk = len(bk)
ek = 'END ENCRYPTED PRIVATE KEY'
lek = len(ek)
top = '-'*((w-lbk)//2) + bk + '-'*((w-lbk)//2)
bottom = '-'*((w-lek)//2) + ek + '-'*((w-lek)//2)
print(f'''
{top}

      _ _        _              
 _ __(_) |_ __ _| |_ ___  _ __  
| '__| | __/ _` | __/ _ \| '_ \ 
| |  | | || (_| | || (_) | |_) |
|_|  |_|\__\__,_|\__\___/| .__/ 
                         |_|    

commands:
    osscs.backend.core.server
    osscs.backend.core.client

{bottom}
''')