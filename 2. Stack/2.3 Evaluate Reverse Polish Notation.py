def eval_rpn(tokens):
	stack = []

	for token in tokens:
		if token in "+-*/":
			operand2 = stack.pop()
			operand1 = stack.pop()

			if token == '+':
				result = operand1 + operand2
			elif token == '-':
				result = operand1 - operand2
			elif token == '*':
				result = operand1 * operand2
			elif token == '/':
				# Note: In Python 3, dividing two integers using '/' performs floating-point division.
				# If you need to perform integer division, you can use '//' instead.
				result = int(operand1 / operand2)

			stack.append(result)
		else:
			stack.append(int(token))

	return stack.pop()


# Example usage:
expression = ["2", "1", "+", "3", "*"]
expression2 = ["2", "1", "*", "5", "+", "3", "*"]
result = eval_rpn(expression)
result_2 = eval_rpn(expression2)
print(result, result_2)  # Output: 9
