def valid_parentheses(s):
	stack = []
	mapping = {")": "(", "]": "[", "}": "{"}

	for char in s:
		if char in mapping:
			first_element = stack.pop() if stack else "#"
			if mapping[char] != first_element:
				return False
		else:
			stack.append(char)

	return not stack


s = "(){}[]"
print(valid_parentheses(s))

s = "({}["
print(valid_parentheses(s))