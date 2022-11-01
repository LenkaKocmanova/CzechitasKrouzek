import random
poc_cislic = 4
poc_pokusu = 10

los = ""

for i in range(poc_cislic):
    los += str(random.randint(0, 9))
# print(los)
j = 0
while True:
    tip = input('Zadej tip: ')
    j+=1
    if tip == los:
        print('Spravne')
        break
    elif j >= poc_pokusu:
        print("Smolicek pacholicek, hledana sifra byla", los)
        break
    else:
        byku = 0
        krav = 0
        for i in range(poc_cislic):
            if los[i] == tip[i]:
                byku +=1
            elif los[i] in set(tip):
                krav += 1
        print('Mas: '+str(byku)+' byku a '+str(krav)+' krav')



