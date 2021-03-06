def isSubsetSum(arr, n, sum):
	if sum == 0:
		return True
	if n == 0 and sum != 0:
		return False

	print(f'Array: {arr}\nLength: {n}\nTotal Sum: {sum}')


	if arr[n-1] > sum:
		return isSubsetSum(arr, n-1, sum)

	#  or isSubsetSum(arr, n-1, sum-arr[n-1])
	# isSubsetSum(arr, n-1, sum)

	return isSubsetSum(arr, n-1, sum-arr[n-1])

def findPartition(arr, n):
	sum = 0
	for i in range(0, n):
		sum += arr[i]

	if sum % 2 != 0:
		return False

	return isSubsetSum(arr, n, sum // 2)
