# A bomaru tree os am prdered tree with the following properties
# Every node has at most two children
# Each child node is labeled as being a left child or right child.
# A left child precedes a right child in the order of children
# A binary tree is proper/full if each node has either zero or two children

# The binary tree ADT
"""
The bin tre is a specialization of a tree, so it inherits the trees methods
plus these additional three accessor methods.
T.left(p): Returns the position of left child, none if empty
T.right(p): Returns the position of right child, none if empty
T.sibling(p): Returns the position of sibling p, none if empty.
"""

class BinaryTree(Tree):
	"""
	Abstract base class representing a binary tree structure.
	
	Additional abstract methods.
	"""

	def left(self, p):
		"""
		Returns a position representing p's left child
		Return None if p doesn't have a child
		"""
		raise NotImplementedError("Must be implemented by subclass")

	def right(self, p):
		"""
		Returns a position rerpresenting p's right child
		Return None if p doesn't have a child
		"""
		raise NotImplementedError("Must be implemented by a subclass")

	def sibling(self, p):
		"""
		Returns a position representing p's siblings(none if no sibling)
		A concrete method implementation
		"""
		parent = self.parent(p)
		if parent is None:				# p must be the root
			return None 				# root has no sibling
		else:
			if p == self.left(parent):
				return self.right(parent)	# possibly None
			else:
				return self.left(parent)	# possibly None	

	def children(self, p):
		"""
		Generates an iteration of Positions represesnting p's children.
		"""
		if self.left(p) is not None:
			yield self.left(p)
		if self.right(p) is not None:
			yield self.right(p)

# In general, level d has at most 2^d nodes.
# The no of external node is no of internal node + 1

# Binary trees can be represented linked(ly) and arrary(ly). 
# I would type code, but long.
