class ArrayExceptSelf():
	def aes_define(self, nums):
		n = len(nums)

		prefix = [1] * n
		suffix = [1] * n

		prefix[0] = 1
		for i in range(1, n):
			prefix[i] = prefix[i - 1] * nums[i - 1]

		suffix[n - 1] = 1
		for i in range(n - 2, -1, -1):
			suffix[i] = suffix[i + 1] * nums[i + 1]

		output = [prefix[i] * suffix[i] for i in range(n)]
		return output


test_aes1 = ArrayExceptSelf()
print(test_aes1.aes_define([1, 2, 3, 4, 5, 6, 7, 8, 9]))