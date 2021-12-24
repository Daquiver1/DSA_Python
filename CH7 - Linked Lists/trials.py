# Python lists are highly optimized but there are a few limitations.
# 1. Length of a dynamic array might be longer than the actual 
# number it stores.
# 2. Ammortized bounds for operations may be unacceptable in real-time systems.
# 3. Insertions and deletions at interior positons of an array are expensive.

# This is where linked lists come in. 
# They are made up of nodes, each node stores a reference to an object and the
# reference to the next node of the list. (Singly)
# Head is first node reference, tail is last node reference. 