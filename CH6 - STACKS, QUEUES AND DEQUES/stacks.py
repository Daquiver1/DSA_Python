# A stack is a collection of objects that are inserted and removed
# accoriding to LIFO principle. So from the top. Access or removal of
# stacks is only allowwed from the top.

# Adapter design pattern is when we want to modify an existing class
# so that its methods match those of a related but different class.
# The adapter design pattern is use to create a stack ADT.

class ArrayStack: 
	"""
	LIFO Stack implementation using a Python list as underlying storage.

	The space usage for a stack is O(n)
	"""

	def __init__(self):
		"""
		Create an empty stack.
		"""
		self._data = []				# nonpublic list instance

	def __len__(self):
		"""
		Return the number of elements in the stack.
		O(1)
		"""
		return len(self._data)

	def is_empty(self):
		"""
		Return True if the stack is empty.

		O(1)
		"""
		return len(self._data) == 0

	def push(self, e):
		"""
		Add element e to the top of the stack
		"""
		self._data.append(e)

	def top(self):
		"""
		Return (but do not remove) the element at the to of the stack.

		Raise Emptyy exception if the stack is empty.
		O(1)
		"""
		if self.is_empty():
			raise Empty("Stack is empty")

		return self._data[-1] 			# the last item in the list

	def pop(self):
		"""
		Remove and return the element from the top of the stack (i.e., LIFO).

		Raise Empty exception if the stack is empty.
		"""
		if self.is_empty():
			raise Empty("Stack is empty")

		return self._data.pop()

# Because of it's LIFO approach, stacks can easily be used for reversing data

def is_matched(expr):
	"""
	Return True if all delimiters are properly match; False otherwise.

	O(n)
	"""

	lefty = "({["
	righty = ")}]"
	S = ArrayStack

	for c in expr:
		if c in lefty:
			S.push(c)		# pushes an opening symbol onto S
		elif c in righty:
			if S.is_empty():
				return False
			if righty.index(c) != lefty.index(S.pop()):
				return False 	# pops an opening symbol when a close symbol is encountered

	return S.is_empty() # if the stack is empty then our expression was well matched.

def is_matched_html(raw):
	"""
	Return True if all HTML tags are properly match; False otherwise.
	"""

	S = ArrayStack()
	j = raw.find("<")		# find first "<" character (if any)

	while j != -1:
		k = raw.find(">", j + 1) # find next ">" character
		if k == -1:
			return False 		# invalid tag
		tag = raw[j+1: k]		# strip away < >
		if not tag.startswith('/'):		# this is opening tag
			S.push(tag)
		else:					# this is closing tag
			if S.is_empty():
				return False 	# nothing to match with
			if tag[1:] != S.pop():
				return False 	# mismtached delimiter
		j = raw.find("<", k + 1)	# find next "<" character (if any)

	return S.is_empty()			# all opening tags matched?