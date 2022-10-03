# Kolik si dáš plátků šunky? 3
# Kolik si dáš plátků sýra? 4
# Kolik máš doma plátků šunky? 12
# Kolik máš doma plátků sýra? 13

sunky = int(input('Kolik si dáš plátků šunky?'))
syra = int(input('Kolik si dáš plátků sýra?'))
sunky_celk = int(input('Kolik máš doma plátků šunky?'))
syra_celk = int(input('Kolik máš doma plátků sýra?'))

toustu_sunk = int(sunky_celk/sunky)
toustu_syr = int(syra_celk/syra)

toustu = toustu_sunk

if(toustu_sunk > toustu_syr):
    toustu = toustu_syr

print('Můžeš si udělat toust až '+str(toustu)+'x!')