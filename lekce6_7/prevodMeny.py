# Zadej cenu 1. položky: 3.49
# Zadej cenu 2. položky: 9.9
# Zadej cenu 3. položky: 47.65
# Zadej cenu 4. položky: q
# Příklad výstupu:
# Převedená cena 1. položky je 75.9773 kč.
# Převedená cena 2. položky je 215.523 kč.
# Převedená cena 3. položky je 1037.3405 kč.

def prevod_na_koruny(v_dolarech):
    int_v_dolarech = float(v_dolarech)
    return ((int_v_dolarech)*21.77)

seznam = []
slovo = ''
polozka = 0
while(slovo != 'q'):
    slovo = input('Zadej cenu '+str(polozka+1)+'. položky: ')
    if (slovo != 'q'):
        seznam.append(slovo)
        polozka += 1

for i in range(polozka):
    print('Převedená cena '+str(i+1)+'. položky je '+str(prevod_na_koruny(seznam[i]))+' kč.')