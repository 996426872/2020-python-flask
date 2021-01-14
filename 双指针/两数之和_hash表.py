"""
给定数组nums，整数之和目标值target
返回数组中两个整数之和等于目标值的数组下标
"""

class Solution(object):
    def twoSum(self, nums, target):
        nums_dict = {}
        for i, num in enumerate(nums):
            if target-num in nums_dict:
                return i, nums_dict[target-num]
            nums_dict[nums[i]] = i


nums_ceshi1 = [2,7,11,15]
target_1 = 9
target_2 = 22
target_3 = 12

solution = Solution()
print(solution.twoSum(nums_ceshi1, target_2))
