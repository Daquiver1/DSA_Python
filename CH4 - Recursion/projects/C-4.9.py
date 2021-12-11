"""
TODO: Write a short recursive Python function that finds
	 the minimum values in a sequence without 
	 using any loops.
"""

def min_max(array, n):
	"""
	Returns the min and max value of sequence array
	"""

	if n == 1: 
		return array[0]
	else:
		min_val = min(array[n-1], min_max(array, n-1))
	return min_val


num = [1,2,3,5,5,3,5,7]
print(f"The min and max value of the above array is {min_max(num, 8)}")