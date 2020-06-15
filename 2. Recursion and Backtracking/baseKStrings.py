def rangeToList(k):
	result = []
	for i in range(k):
		result.append(str(i))
	return result

def baseKString(n, k):
	if n == 0:
		return []
	if n == 1:
		return rangeToList(k)
	return [digit + bitstring for digit in baseKString(1, k) for bitstring in baseKString(n-1, k)]

print(baseKString(2, 3))