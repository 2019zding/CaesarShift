def caesarShift(input, increase):
	decrypt = []
	encrypt = []

	alpha = list('abcdefghijklmnopqrstuvwxyz')
	for eachLetter in input:
		if eachLetter in alpha:
			index = alpha.index(eachLetter)
			crypting = (index + increase) % 26
			encrypt.append(crypting)
			newLetter = alpha[crypting]
			decrypt.append(newLetter)
	return decrypt
code = caesarShift('gdkkn', 1)
print(code)
code2 = caesarShift('umpjb', 2)
print(code2)
code3 = caesarShift('yvb', 3)
print(code3)
