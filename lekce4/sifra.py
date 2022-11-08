# Zadej slovo, nebo pořadí pro ukončení: doba
# Zadej slovo, nebo pořadí pro ukončení: trumpeta
# Zadej slovo, nebo pořadí pro ukončení: Zimbabwe
# Zadej slovo, nebo pořadí pro ukončení: Uf!
# Zadej slovo, nebo pořadí pro ukončení: 3
# Příklad výstupu:
# Šifra zní: bum!

pole = []
while (True):
    slovo = input('Zadej slovo, nebo pořadí pro ukončení: ')
    if slovo.isdecimal():
        poradi = int(slovo)
        break
    pole.append(slovo)

sifra = ''
for i in range(len(pole)):
    sifra += pole[i][poradi-1]

print('Šifra zní: '+ sifra)

