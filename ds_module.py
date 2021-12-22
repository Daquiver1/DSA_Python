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
