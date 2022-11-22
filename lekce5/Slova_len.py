# Zadej slovo: lemra
# Zadej slovo: povaleč
# Zadej slovo: vokurka
# Zadej slovo: spáč
# Zadej slovo: q
# Vyber pořadí slova v žebříčku: 2
# Příklad výstupu:
# 2. slovo v pořadí je: lemra

seznam = []
slovo = ''
while(slovo != 'q'):
    slovo = input('Zadej slovo: ')
    if (slovo != 'q'):
        seznam.append(slovo)

novy_seznam = sorted(seznam, key=len) # sorts by descending length
print(novy_seznam)
poradi = int(input('Vyber pořadí slova v abecedním žebříčku: '))
print(str(poradi) + '. slovo v pořadí je: ' + novy_seznam[poradi - 1])