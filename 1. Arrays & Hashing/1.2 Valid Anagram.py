def is_anagram(slovo, slovo_2):
	if len(slovo) != len(slovo_2):
		return False

	slovar = {}

	for s in slovo:
		if s in slovar:
			slovar[s] += 1
		else:
			slovar[s] = 1

	for s in slovo_2:
		if s in slovar:
			slovar[s] -= 1
		else:
			return False

	return all(count == 0 for count in slovar.values())

print(is_anagram("anagram", "anagram"))
print(is_anagram("nagra", "anagram"))