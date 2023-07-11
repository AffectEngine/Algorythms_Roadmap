class Solution(object):
	def twoSum(self, nums, target):
		num_dict = {}
		for i, num in enumerate(nums):
			complement = target - num
			if complement in num_dict:
				return [num_dict[complement], i]
			num_dict[num] = i
		return []

sol1 = Solution()
print(sol1.twoSum([1, 2, 3, 4], 7))

sol2 = Solution()
print(sol2.twoSum([11, 22, 33, 44], 3))