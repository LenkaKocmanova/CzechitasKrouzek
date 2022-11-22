# Zadej slovo: lemra
# Zadej slovo: vokurka
# Zadej slovo: povaleč
# Zadej slovo: spáč
# Zadej slovo: q
# Vyber pořadí slova v abecedním žebříčku: 2
# Příklad výstupu:
# 2. slovo v abecedním pořadí je: povaleč
import numpy as np

seznam = []
slovo = ''
while(slovo != 'q'):
    slovo = input('Zadej slovo: ')
    if (slovo != 'q'):
        seznam.append(slovo)

novy_seznam = np.sort(seznam)
print(novy_seznam)
poradi = int(input('Vyber pořadí slova v abecedním žebříčku: '))
print(str(poradi) + '. slovo v abecedním pořadí je: ' + novy_seznam[poradi - 1])