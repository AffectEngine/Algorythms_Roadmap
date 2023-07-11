class DefineDuplicate:
	def define_duplicate(self, nums):
		if len(nums) == len(set(nums)):
			return False
		else:
			return True


duplicate_test1 = DefineDuplicate()
print(duplicate_test1.define_duplicate([1, 2, 3, 4, 5, 6]))
duplicate_test2 = DefineDuplicate()
print(duplicate_test2.define_duplicate([1, 2, 3, 4, 5, 6, 6]))
