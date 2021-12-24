# Implementing a stack with a singly linked list
class LinkedStack:
	"""
	LIFO Stack implementation using a singly linked list for storage.

	The worst cast for all the operations is O(1) and O(n) for space
	"""

	#_______________nested _Node class___________
	class _Node:
		"""
		Lightweight, nonpublic class for storing a singly linked node.
		"""

		__slots__ = "_elements", "_next"	# streamline memory usage

		def __init__(self, element, next):	# initialize node's fields
			self._element = element			# reference to user's element
			self._next = next 				# reference to next node

	#____________ stack methods_____________
	def __init__(self):
		"""
		Create an empty stack. 
		"""
		self._head = None		# reference to the head node
		self._size = 0 			# number of stack elements

	def __len__(self):
		"""
		Return the number of elements in the stack.
		"""
		return self._size

	def is_empty(self):
		"""
		Return True if the stack is empty.
		"""
		return self._size == 0

	def push(self, e):
		""" 
		Add element e to the top of the stack.
		"""
		self._head = self._Node(e, self._head)
		self._size += 1

	def top(self):
		"""
		Return (but do not remove) the element at the top of the stack.

		Raise Empty exception if the stack is empty.
		"""
		if self.is_empty():
			raise Empty("Stack is empty")

		return self._head._element 			# top of stack is at head of list

	def pop(self):
		"""
		Remove and return the element from top of stack.

		Raise Empty exception if the stack is empty.
		"""
		if self.is_empty():
			raise Empty("Stack is empty")

		answer = self._head._element 
		self._head = self._head._next		# bypass the former top node.
		self._size -= 1
		return answer

# Implementing a queue with a singly linked list
class LinkedQueue:
	"""
	FIFO queue implementation using a singly linked list for storage.
	"""

	class _Node:
		"""
		Lightweight, nonpublic class for storing a singly linked node.
		"""

		__slots__ = "_elements", "_next"	# streamline memory usage

		def __init__(self, element, next):	# initialize node's fields
			self._element = element			# reference to user's element
			self._next = next 				# reference to next node

	def __init__(self):
		"""
		Create an empty queue.
		"""
		self._head = None
		self._tail = None
		self._size = 0 						# number of queue elements

	def __len__(self):
		"""
		Return the number of elements in the queue.
		"""
		return self._size

	def is_empty(self):
		"""
		Return True if the queue is empty.
		"""
		return self._size == 0

	def first(self):
		"""
		Return(don't remove) the element at the front of the queue.
		"""
		if self.is_empty():
			raise Empty("Queue is empty")

		return self._head._element 				# front alinged with head of list

	def dequeue(self):
		"""
		Remove and return the first element of the queue.

		Raise Empty exception if the queue is empty.
		"""
		if self.is_empty():
			raise Empty("Queue is empty")


		answer = self._head._next
		self._size = self._head._next
		self._size -= 1
		if self.is_empty():
			self._tail = None

		return answer

	def enqueue(self, e):
		"""
		Add an element to the back of the queue
		"""
		newest = self._Node(e, None)
		if self.is_empty():
			self._head = newest
		else:
			self._tail._next = newest

		self._tail = newest
		self._size += 1