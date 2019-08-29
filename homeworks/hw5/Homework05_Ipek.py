## Ipek Ece Sener
## Homework 5

class Node:
	def __init__(self, _value=None, _next=None):
		self.value = _value
		self.next = _next
	def __str__(self):
		return str(self.value)
	def get_value(self):
		return self.value
	def get_next(self):
		return self.next 
	def set_next(self, new_next):
		self.next = new_next

class LinkedList:
	def __init__(self, value):
		node = Node(value)
		self.root = node
		self.next = node.next
		self.length = 1
	def __str__(self):
		head = self.root
		while head:
			print(str(head))
			head = head.next
		return " "
	def length(self):
		return self.length
	def addNode(self, new_value):
		if not self.root:
			self.root = Node(new_value)
			return
		current = self.root
		while current.next:
			current = current.next
		current.next = Node(new_value)
	def removeNode(self, node_to_remove):
		current = self.root
		previous = None
		while current and current.value != node_to_remove:
			previous = current
			current = current.next 
		if previous is None:
			self.root = current.next
		elif current:
			previous.next = current.next
			current.next = None





