#
# Je přítomen štípač? ano/ne: ano
# Je přítomen utěrač potu? ano/ne: ano
# Je přítomen instruktor? ano/ne: ano
# Příklad výstupu:
# No a je to!

dotaz = input('Je přítomen štípač? ano/ne:')
if (dotaz == 'ano'):
    stipac = True
else:
    stipac = False
dotaz = input('Je přítomen utěrač potu? ano/ne:')
if (dotaz == 'ano'):
    uterac = True
else:
    uterac = False
dotaz = input('Je přítomen instruktor? ano/ne:')
if (dotaz == 'ano'):
    instruktor = True
else:
    instruktor = False

if((stipac and uterac and instruktor) or (not uterac and instruktor)):
    print('No a je to!')
else:
    print('Aaaa bum!')
