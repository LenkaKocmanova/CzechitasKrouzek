import random

cisla = random.sample(range(1, 25), random.randint(1, 9))

#########
nova_cisla = []
for cislo in cisla:
    cislo = str(cislo)
    nova_cisla.append(cislo)
s = "-"

s = s.join(nova_cisla)
print(s)
#########