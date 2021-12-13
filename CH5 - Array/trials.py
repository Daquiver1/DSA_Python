
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
# it calls for more space,So now it's 15. it calls for more space by creating a new array that 
# references the objects, then deletes the old alias. WOW!. Here's proof.

import sys
data = []
for k in range(20):
	a = len(data)			# number of elements
	b = sys.getsizeof(data)		# actual size in bytes
	print(f"Length: {a}, Size in bytes: {b}")
	data.append(None)		# increase length by one

# Because a list is a referential structure, getsizeof only inludes the size
# forrepresentiing the primary structure, doesn't account for memory used 
# by objectss the are elements of the list.
# When "growing" an array the main issue is how large to create a new array,
# a common rule is for the new array to have twice the capacity of the old

# Tuples are generally more memory efficient than lists, because they are immutable.
def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until 
        # an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key


data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)