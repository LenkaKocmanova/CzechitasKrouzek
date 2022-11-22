# Tah hráče 1: 3 4
# Tah hráče 2: 2 3
# Tah hráče 1: 4 5

pole = []
for i in range(5):
    temp = []
    for j in range(5):
        temp.append('_')
    pole.append(temp)

hrac = 1
vstup = ''
while(vstup != 'q'):
   vstup = (input('Tah hrace '+str(hrac)+': '))
   if (vstup != 'q'):
       vystup = vstup.strip(" ").split(' ')
       if(hrac == 1):
           pole[int(vystup[0]) - 1][int(vystup[1]) - 1] = 'X'
           hrac = 2
       else:
           pole[int(vystup[0]) - 1][int(vystup[1]) - 1] = 'O'
           hrac = 1
       print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                        for row in pole]))