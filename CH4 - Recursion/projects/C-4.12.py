"""
TODO: Give a recursive algorithm to compute the product of
	 two positive integers, m and n, using only addition and subtraction.
"""

def multiply(m, n):
	if n == 1:
		result = m 
	else:
		result = m + multiply(m, n-1)

	return result

print(f"The product of two positive integers 4 and 12 is {multiply(4, 12)}")
