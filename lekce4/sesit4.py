# import time
# CAS = 1
#
# #########
#
# odpocet = range(10, 0, -1)
#
# #########
#
# for sekunda in odpocet:
#   print(sekunda)
#   time.sleep(CAS)
# print("Zážeh!")

casy_zavodniku = [14.93, 10.18, 19.35, 10.04, 12.99, 17.19, 17.99, 12.04, 19.16, 7.72, 17.87, 8.29, 12.9, 17.41, 8.62]

i = 0
for cas in casy_zavodniku:
  if(cas>=9.0):
    continue
  print(cas)
  i += 1
  print("To byl čas " + str(i) + ". závodníka.")