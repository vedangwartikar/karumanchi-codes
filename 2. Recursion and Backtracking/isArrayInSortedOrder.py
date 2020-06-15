def isArrayInSortedOrder(A):
	if len(A) == 1:
		return True
	return A[0] <= A[1] and isArrayInSortedOrder(A[1:])
A = [127, 148, 99, 144]
print(isArrayInSortedOrder(A))