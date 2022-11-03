# Zadej 1 (kámen),
# 2 (nůžky),
# nebo 3 (papír): 1
# Příklad výstupu:
# Volím 2!
# Vyhráváš proti stroji.

import random

moje_volba = int(input('Zadej 1 (kámen), 2 (nůžky), nebo 3 (papír):'))
pc_volba = random.randint(1,3)
print(pc_volba)
if(moje_volba>=1 and moje_volba<=3):
    if(pc_volba == 1):
        print('PC volí kámen')
    if (pc_volba == 2):
        print('PC volí nůžky')
    if (pc_volba == 3):
        print('PC volí papír')
    if((moje_volba ==(pc_volba-1))or((moje_volba == (pc_volba-2)))):
        print('Vyhráváš proti stroji.')
    elif ((moje_volba ==(pc_volba+1))or((moje_volba == (pc_volba+2)))):
        print('Prohráváš proti stroji.')
    elif (moje_volba ==pc_volba):
        print('Remiza.')
else:
    print('Zadal jsi spatne cislo!')

