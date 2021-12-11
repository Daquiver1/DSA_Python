# Text Demaris

# Python represents each character with 2 bytes(16 bits)
# So a six-character string (SAMPLE) will bstored in 12 consecutive bytes
# of memory.

# Each cell of an array must have the same number of bytes.
# This becomes a bit complicated when dealing with strings of diff lengths.
# Python overcomes this by storing object of references. So the array will
# contain the memory address of the names. This way one can still index in O(1)
# since they are next to each other. 

# Lists and tuples are referential structures.
# Strings are represented using an array of characters not references(lists, tuples)
# This is called compact array
# When you slice a list, the new list you get still points to the same
# object as the old list.
# When you change the element in a slice list,it doesn't affect the old list
# because it justs points to a new object, instead of changing the old object.
# 

temp = [1,2,3,4,5,6,8]
new = temp[1:4]
new[2] = 29 # points to a new object, so temp stays unchanged.
print(new)
print(temp)

# In terms of space, compact arrays are more efficent than referential 
# structures
# Support for compact arrays is in a module named array.

# Python lists uses dynamic array. Say when you create a list of 5 elements,
# the system creates an array of lets say 8 instead. When the lists exhausts those 8
# it calls for more space, so now it's 15. Here's proof.

import sys
data = []
for k in range(20):
	a = len(data)			# number of elements
	b = sys.getsizeof(data)		# actual size in bytes
	print(f"Length: {a}, Size in bytes: {b}")
	data.append("a")		# increase length by one
