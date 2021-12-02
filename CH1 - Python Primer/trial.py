# A list  begins with []
# list("Hello") will a return a list of h e l l o
# A tuple begins with ()
# A set begins with {}
# set("hello") will return a set of h e l l o
# A set uses a hash table to maintain it's uniqueness.
# A dictionary begins with {}
alpha = [1,2,3]
beta = alpha  # an alias for alpha
beta += [4,5]  # extends the original list with 2 more elements
beta = beta + [6,7]  # reassigns beta to a new list [1,2,3,4,5,6,7]
print(alpha)  # will be [1,2,3,4,5]

# Polymorphic functions support more than one possible calling signature
def count(a, b=2, c=4):
	pass

# Count is polymorphic because you can call it by 
# count(2)
# count(4, 5)

# With reading files
# .read will read the entire contents of the file as a string.
# .readline will return the current line as a string
# .readlines will return all the remanining lines as a list of strings.
