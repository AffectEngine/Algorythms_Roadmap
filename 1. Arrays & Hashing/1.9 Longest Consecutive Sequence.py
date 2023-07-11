class Solution():
	def longestConsecutive(self, nums):
		new_set = set(nums)
		max_len = 0

		for num in nums:
			if num - 1 not in new_set:
				curr_num = num
				curr_len = 1

				while curr_num + 1 in new_set:
					curr_num += 1
					curr_len += 1

				max_len = max(max_len, curr_len)

		return max_len


testcase1 = Solution()
print(testcase1.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1, 26, 25, 24, 23]))
