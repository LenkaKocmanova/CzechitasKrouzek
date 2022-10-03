# Kolik surovin dáme do toustu? 3
# Kolik si dáš plátků 1. suroviny? 3
# Kolik si dáš plátků 2. suroviny? 4
# Kolik si dáš plátků 3. suroviny? 7
# Kolik máš doma plátků 1. suroviny? 12
# Kolik máš doma plátků 2. suroviny? 13
# Kolik máš doma plátků 3. suroviny? 18
# Příklad výstupu:
# Můžeš si udělat toust až 2x!

surovin = int(input('Kolik surovin dáme do toustu?'))
polozka = []
polozka_celk = []
polozka_toustu = []
for i in range(surovin):
    polozka.append(int(input('Kolik si dáš plátků '+str(i+1)+'. suroviny?')))


for i in range(surovin):
    polozka_celk.append(int(input('Kolik máš doma plátků '+str(i+1)+'. suroviny?')))
    polozka_toustu.append(int(polozka_celk[i]/polozka[i]))


print('Můžeš si udělat toust až '+str(min(polozka_toustu))+'x!')

