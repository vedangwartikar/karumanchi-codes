def appendAtBeginningFront(x, L):
	return [x + element for element in L]

def bitStrings(n):
	if n == 0:
		return []
	if n == 1:
		return ['0', '1']
	else:
		return (appendAtBeginningFront('0', bitStrings(n-1)) + appendAtBeginningFront('1', bitStrings(n-1)))

print(bitStrings(3))


def bitStrings(n):
	if n == 0:
		return []
	if n == 1:
		return ['0', '1']
	return [digit + bitstring for digit in bitStrings(1) for bitstring in bitStrings(n-1)]

print(bitStrings(3))