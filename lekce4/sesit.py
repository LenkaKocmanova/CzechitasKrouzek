print("↓↓↓↓ Úloha 4.f ↓↓↓↓")
# 4.f
# Projdi postupně řetězec "hlaska" zadaný uživatelem a každé písmeno vypiš na nový řádek. Nápověda: Pokud si nevzpomínáš, jak lze takto projít řetězec, zkus ho použít do cyklu for jako procházenou sekvenci.

hlaska = input("Zadej nějaký řetězec: ")

#########

# tvůj kód

#########


print("↓↓↓↓ Úloha 4.g ↓↓↓↓")
# 4.g
# Ze seznamu "verze_windows" vypiš postupně každý prvek s lichým indexem. Nápověda: Postačí ti funkce range(). Vyzkoušej si, co dělají její tři parametry.

verze_windows = ["Windows Me", "Windows XP", "Windows Vista", "Windows 7", "Windows 8", "Windows 10", "Windows 11"]
print("Kvalitní verze OS Windows byly: ")

#########

# tvůj kód

#########


print("↓↓↓↓ Úloha 4.h ↓↓↓↓")
# 4.h
# Vytvoř seznam "odpocet", který bude obsahovat čísla v pořadí od 10 do 1, tak abychom následující kód mohli prodat do Ameriky podniku NASA.

import time

CAS = 1

#########

# tvůj kód

#########

for sekunda in odpocet:
    print(sekunda)
    time.sleep(CAS)
print("Zážeh!")

print("↓↓↓↓ Úloha 4.i ↓↓↓↓")
# 4.i
# Vypiš každý čas závodníka ze seznamu "casy_zavodniku", který má čas nižší než 9 sekund. Ostatní ignoruj (tedy přeskoč)!

casy_zavodniku = [14.93, 10.18, 19.35, 10.04, 12.99, 17.19, 17.99, 12.04, 19.16, 7.72, 17.87, 8.29, 12.9, 17.41, 8.62]

i = 0
for cas in casy_zavodniku:
    #########

    # tvůj kód

    #########
    i += 1
    print("To byl čas " + str(i) + ". závodníka.")

print("↓↓↓↓ Úloha 4.j ↓↓↓↓")
# 4.j
# Vypisuj postupně každý čas závodníka ze seznamu "casy_zavodniku", dokud nenarazíš na závodníka s časem větším než 11 sekund. Pak skonči.

casy_zavodniku = [14.93, 10.18, 19.35, 10.04, 12.99, 17.19, 17.99, 12.04, 19.16, 7.72, 17.87, 8.29, 12.9, 17.41, 8.62]
casy_zavodniku.sort()

for cas in casy_zavodniku:
#########

# tvůj kód

#########


print("↓↓↓↓ Úloha 4.k ↓↓↓↓")
# 4.k pro zapálené
# Vypiš náhodný seznam čísel "cisla" v jednom řádku ve formátu "1 - 2 - 3 - 4 - ..." a tak dále. Nápověda: Zkus prozkoumat metodu .join(seznam) datového typu string. Nápověda 2: Nezapomeň zajistit, aby datové typy v seznamu byly typu string.

import random

cisla = random.sample(range(1, 25), random.randint(1, 9))

#########

# tvůj kód

#########