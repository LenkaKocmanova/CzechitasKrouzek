# Kolik mi zadáš knížek? 5
# Zadej název 1. knížky: Honzíkova cesta
# Zadej název 2. knížky: Stmívání
# Zadej název 3. knížky: Bible
# Zadej název 4. knížky: Emil, čili o výchově
# Zadej název 5. knížky: Grey
# Příklad výstupu:
# Seřadil jsem ti knížky:
# ['Bible', 'Emil, čili o výchově',
# 'Grey', 'Honzíkova cesta', 'Stmívání']

pocet = int(input('Kolik mi zadáš knížek? '))
seznam = []
for i in range(pocet):
    pomocna = input('Zadej název '+ str(i+1) +'. knížky: ')
    seznam.append(pomocna)

seznam.sort()
print('Seřadil jsem ti knížky:')
print(seznam)