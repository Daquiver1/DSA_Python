# Recursion is the technique by which a function calls itself during 
# execution

# Factorial tells us the possible distinct ways n items can be arranged.
# 3!(abc) = 6( abc, acb, bac, bca, cab, cba)

def factorial(n):
	if n == 0:
			return 1
	else: 
		return n * factorial(n-1)

num = 5
print(f"The factorial of {num} is {factorial(num)}")

# Each time a function is called an activation record or frame
# is created to store information, practically a namespace.
# Each function call has it's own dedicated activation record.

def binary_search(data, target, low, high):
	""" 
	Return True if target is found in indicated portion of a Python List

	The search only considers the portion from data[low] to data[high] inclusive
	"""
	if low > high:
		return False
	else:
		mid = (low + high)//2
		if target == data[mid]:
			return True  
		elif target < data[mid]:
			# recursion on the left of mid
			return binary_search(data, target, low, mid-1)
		else:
			# recursion on the right of mid
			return binary_search(data, target, mid + 1, high)

def bad_fibonaacci(n):
	"""
	Returns the nth fibonacci number
	This format of fib is very inefficent due to the number of 
	calls it'll have to make.
	If you study the number of calls, you'll notice the efficency is O(n^2)

	"""
	if n <=1:
		return n
	else:
		return bad_fibonaacci(n-2) + bad_fibonaacci(n-1)

def good_fibonacci(n):
	""" 
	Returns par of Fibonacci numbers, F(n) and F(n-1)
	This format is more efficent
	"""
	if n <= 1:
		return(n, 0)
	else:
		(a,b) = good_fibonacci(n-1)
		return (a+b, a)

import sys
old = sys.getrecursionlimit() #  Old recursion limit, it's a 1000
sys.setrecursionlimit(1000000) #  Change Recursion limit

def linear_sum(S, n):
	""" 
	Returns the sum of the first n numbers of a sequence S
	Handles it recursively.
	It takes O(n) for both time and space
	"""
	if n == 0:
		return 0 
	else:
		return linear_sum(S, n-1) + S[n-1]

def reverse(S, start, stop):
	""""
	Reverse elements in implicit slice S[start:stop].
	Handles it recursively.
	Runs in O(n)
	"""
	if start <stop - 1: # If at least 2 elements
		S[start], S[stop-1] = S[stop - 1], S[start] # Swap first and last
		reverse(S, start+1, stop-1) # recur on rest
	return S



num = [1,2,3,4,5,7,5,7,6]
print(f"The sum of the above list is {linear_sum(num,9)}")
print(f"The reversal of the above list is {reverse(num,0, len(num))}")

# A linear recursion is one that calls only one function. See reverse
# A binary recursion is one that calls two functions. See bad_fibonacci
# A multiple recursion is one that calls 2+ functions. 
"""
When designing recursive algorithms, think and test for a base case, each call 
must end up at a base case. Then recur
"""