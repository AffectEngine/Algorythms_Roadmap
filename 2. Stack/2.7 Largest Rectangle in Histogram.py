def largestRectangleArea(heights):
	stack = []
	maxArea = 0
	n = len(heights)

	for i in range(n):
		while stack and heights[i] < heights[stack[-1]]:
			height = heights[stack.pop()]
			width = i if not stack else i - stack[-1] - 1
			area = height * width
			maxArea = max(maxArea, area)

		stack.append(i)

	while stack:
		height = heights[stack.pop()]
		width = n if not stack else n - stack[-1] - 1
		area = height * width
		maxArea = max(maxArea, area)

	return maxArea


histogram = [2, 1, 5, 6, 2, 3, 9, 9]
print(largestRectangleArea(histogram))