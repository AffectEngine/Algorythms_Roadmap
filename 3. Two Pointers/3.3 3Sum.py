def threeSum(nums):
    nums.sort()  # Step 1
    result = []
    n = len(nums)

    for i in range(n - 2):  # Step 2
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicates

        second = i + 1
        last = n - 1

        while second < last:  # Steps 3 to 7
            total = nums[i] + nums[second] + nums[last]

            if total < 0:
                second += 1
            elif total > 0:
                last -= 1
            else:
                result.append([nums[i], nums[second], nums[last]])

                while second < last and nums[second] == nums[second + 1]:
                    second += 1  # Skip duplicates
                while second < last and nums[last] == nums[last - 1]:
                    last -= 1  # Skip duplicates

                second += 1
                last -= 1

    return result


nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))