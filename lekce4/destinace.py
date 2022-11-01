# industries_list = [s.split(',') for s in industries_list]
# Zadej svoje navštívené destinace oddělené
# čárkou:
# Helsinky, Oslo, Helsinky, Brusel, Brusel
# Příklad výstupu:
# Protrajdal jsi 3 destinace:
# Helsinky
# Oslo
# Brusel
destinace = input('Zadej svoje navštívené destinace oddělené čárkou: ')
destinace = destinace.split(', ')
i = 0
while i < len(destinace):
	j = i + 1
	while j < len(destinace):
		if destinace[i] == destinace[j]:
			destinace.pop(j)
		else:
			j += 1
	i += 1

print("Protrajdal jsi", len(destinace), "destinace:")
print(", ".join(destinace))