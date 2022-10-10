hlaska = ("Už nikdy nebudu koukat na anime.")
#hlaska = hlaska + " " + hlaska + " " + hlaska
hlaska = (hlaska + " ") *3
print(hlaska)

from datetime import datetime
rok = datetime.now().year

vek = input('Kolik ti je?')
budoucnost = input('Jaký rok tě zajímá?')
rozdil = int(budoucnost) - rok
vek_bud = int(vek) + rozdil
print('V roce '+budoucnost+' ti bude '+str(vek_bud)+' let, trilobite.')


