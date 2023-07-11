def dailyTemperatures(temperatures):
	stack = []
	result = [0] * len(temperatures)

	for i, temp in enumerate(temperatures):
		while stack and temp > temperatures[stack[-1]]:
			prev_index = stack.pop()
			result[prev_index] = i - prev_index
		stack.append(i)

	return result


temperatures = [23, 24, 25, 21, 19, 22, 26, 24]
print(dailyTemperatures(temperatures))
