class MinStack:
	def __init__(self):
		self.stack = []
		self.min_stack = []

	def push(self, x):
		self.stack.append(x)
		if not self.min_stack or x <= self.min_stack[-1]:
			self.min_stack.append(x)

	def pop(self):
		if self.stack[-1] == self.min_stack[-1]:
			self.min_stack.pop()
		self.stack.pop()

	def top(self):
		return self.stack[-1]

	def getMin(self):
		return self.min_stack[-1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.stack)
print(minStack.min_stack)
print(minStack.getMin())
minStack.pop()
print(minStack.stack)
print(minStack.top())
print(minStack.getMin())
