# Tree is a nonlinear data structure.
# A tree is an abstract data type that stores elements hierarchically.
# The formal definiton is a set of nodes storing elements such that there
# is a parent-child relationship. 

# External nodes also known as leaves don't have any childred.
# Internal nodes have children(obviously)

# Root is the main node(top level)
# Edges are the link between two nodes where the relationship is parent to child.
# A tree with n nodes has a max of n-1 edges.
# Parents are nodes that have a child. So all except leaves.
# Children are nodes that have a parent. So all save root.
# Siblings have the same parents.
# A leaf node doesn't have a child.
# Degree of a node is the total number of children it has.
# Level is the step from top to bottom. Where root node is at level 0. 
# Height of a node is the number of vertices from leaf node to it.
# The height of the root node is considered the height of the tree.
# The depth of a node is the number of edges from root to it.
# The depth of leaf nodes is the depth of the tree.
# Path is the sequence of nodes and edge between two nodes. 
# Length of a path is the number of nodes in that path.
# Each child from a node forms a subtree recursively.
# Ancestors are nodes on the path from node to root.
# Descendants are opposite.
# an ordered tree is a tree where the order of the nodes/vertes are significant.

# The tree ADT
"""
The nodes have a name and what is stored in them. Their name is referred to
as position and what they contain is element. 

p.element() - Return the element stored at positon p
T.root() - Returns the root position, None if T is empty
T.is_root(p) - Returns True if position p is the root of Tree
T.parent(p) - Returns the parent of position p. None if p is root.
T.num_children(p) - Returns the number of childred of position p
T.children(p) - Generates an iteration of the children of position p
T.is_leaf(p) - Return True if position p has no children.
len(T) - Returns the number of position(so elements), in tree T.
T.is_empty - Retur True if tree T doesn't have any position.
T.positions() - Generates an iteration of all position of tree T
iter(T) - Gerenates an iteration of all elements stored in T
"""

