# A traversal of a tree T is a systematic way of accessing or visiting all 
# the positions of T.

# Preorder traversal
"""
In preorder traversal of a tree T, the root of T is viistied first and then
the subtrees rooted at it's children are traversed recursively. Left to right
parent => left subtree => right subtree
"""
def preorder(self):
	"""
	Generate a preorder iteration of positions in tree.
	"""
	if not self.is_empty():
		for p in self._subtree_preorder(self.root()): 		# start recursion
			yield p

def _subtree_preorder(self, p):
	"""
	Generate a preorder iteration of positions in subtree rooted at p
	"""
	yield p 								# visit p before its subtrees.
	for c in self.childred(p):				# for each child c
		for other in self._subtree_preorder(c):	# do preorder of c's subtrees
			yield other						# yielding each to our caller


# Postorder traversal
"""
In postorder traversal of a tree T, it traverses subtrees rooted at the children
of root first and visits the root. Left to right. So opposite to preorder.
left subtree => right subtree => parent
"""
def postorder(self):
	"""
	Generate a postorder iteration of positions in the tree.
	"""
	if not self.is_empty():
		for p in self._subtree_postorder(self.root()): 		# start recursion
			yield p	

def _subtree_preorder(self, p):
	"""
	Generate a postorder iteration of positions in subtree rooted at p
	"""
	yield p 								# visit p before its subtrees.
	for c in self.childred(p):				# for each child c
		for other in self._subtree_postorder(c):	# do postorder of c's subtrees
			yield other						# yielding each to our caller


# Inorder traversal(only applies to binary trees)
"""
In inorder traversal of a tree T, it traverses left subtree moves to the tree
and back to right subtree.
left subtree => parent => right subtree
"""

# Breadth-First tree traversal
"""
Adjacency List: O(V+E) vertice and edge
Adjacency Matrix: O(V^2) 

This a traversal which uses a queue data structure(fifo).
It works by taking the root, then all children then all children of child A
It's slower than dfs. In bfs one vertex is selected at a time, when it's
visited and marked then it's adjacent are visited and stored in queue.
"""

# Depth-First tree traversal
"""
Adjacency List: O(V+E)
Adjacency Matrix: O(V^2)

This is a traversal which uses a stack data structure(lifo).
It works by taking all the children of a parent, then moves to next.
It's faster than bfs. In dfs, first visited vertices(parent) are
pushed into stack and if there are no more vertices(children)
then the visited vertices are popped.
"""

# Binary search tree
"""
This is a node-based binary tree data sturcutre whereby
1. The left subtree of a node contains only nodes with keys(elements)
less than the node's key(parent of node).
2. The right subtree of a node contains only nodes with keys greater 
than the node's key(parent of key).
3. The left and right subtree must be a binary search tree.
"""