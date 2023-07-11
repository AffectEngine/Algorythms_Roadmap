def twoSum(numbers, target):
	left = 0
	right = len(numbers) - 1

	while left < right:
		current_sum = numbers[left] + numbers[right]

		if current_sum == target:
			return [left + 1, right + 1]
		elif current_sum < target:
			left += 1
		else:
			right -= 1

	return []  # No solution found


numbers = [2, 7, 11, 15]
target = 18
print(twoSum(numbers, target))  # Output: [1, 2]

numbers = [2, 3, 4]
target = 6
print(twoSum(numbers, target))  # Output: [1, 3]

numbers = [-1, 0]
target = -1
print(twoSum(numbers, target))  # Output: [1, 2]
