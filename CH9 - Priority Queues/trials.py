# It's a priority queue. So queue but items with high priority 
# are settled first. 

# Priority Queue ADT
"""
P.add(k, v): Insert an item with key K and value v into priority queue P
P.min(): Return a tuple, (k,v) representing the key and value of an item
in P with minimum key.
P.remove_min(): Remove the item with minimum key from P
p.is_empty(): Return True if prioirty queue P doesn't contain any items.
len(p): Return the number of items in priority queue P.
"""
# Heaps are an efficient ralization of priority queues. 
# A heab is a binary tree that stores a collection of items at its positions

# In a heap tree, the value in a node is always smaller than both
# of its children. This is called heap property.

# When making heap a list, visualize the elements as a tree. So say
a = [1,2,3,5,6,7,8]
# 1(root) has children 2 and 3
# 2 and 3(parents) have childred 5,6 and 7,8 respectively. You barb.?
