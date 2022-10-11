#
# Je přítomen štípač? ano/ne: ano
# Je přítomen utěrač potu? ano/ne: ano
# Je přítomen instruktor? ano/ne: ano
# Příklad výstupu:
# No a je to!

stipac = input('Je přítomen štípač? ano/ne:') == 'ano'
uterac = input('Je přítomen utěrač potu? ano/ne:') == 'ano'
instruktor = input('Je přítomen instruktor? ano/ne:') == 'ano'
if((stipac and uterac and instruktor) or (not uterac and instruktor)):
    print('No a je to!')
else:
    print('Aaaa bum!')
