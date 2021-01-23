"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：
输入：nums = []
输出：[]
示例 3：
输入：nums = [0]
输出：[]

"""


class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        length = len(nums)
        # print(nums)
        if length < 3:
            return []
        all_three = []
        for k in range(0, length):
            left_flag_top = (k != 0 and nums[k] == nums[k - 1])
            if left_flag_top:
                continue
            a = nums[k]
            target = -a
            all_two = self.twoSum(nums[k+1::], target)
            # 查找到元素后
            if all_two:
                # print("三元素组合a={}，b,c={}".format(a, all_two))
                for two in all_two:
                    all_three.append([a]+two)
                # print("组合后：", all_three)
            # else:
                # print("没有找到匹配的a+b+c=0,a=",a)
        return all_three

    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers) - 1
        all_ele = []
        while i < j:
            # and numbers[i] != numbers[i - 1] and numbers[j] != numbers[j + 1]
            # 非左边界，左边元素重复；左指针向右一步
            left_flag = (i != 0 and numbers[i] == numbers[i-1])
            # 非右边界，右边元素重复；右指针向左一步
            right_flag = (j != (len(numbers)-1) and numbers[j] == numbers[j+1])
            # 左指针元素+右指针元素
            temp = numbers[i] + numbers[j]
            # 左指针元素重复 或者 两元素小于目标值，左指针右移
            if left_flag or temp < target:
                i = i + 1
            # 右指针元素重复 或者两元素大于目标值，右指针左移
            if right_flag or temp > target:
                j = j - 1
            # 两元素之和等于目标值 且 左右指针元素不是已经添加过的，把元素添加进数组
            if temp == target and (not (left_flag or right_flag)):
                all_ele.append([numbers[i], numbers[j]])
                i = i + 1
        return all_ele


nums_ceshi1 = [2, 7, 11, 11, 11, 15]
nums_ceshi2 = [-2, 2, 2, 7, 11, 11, 15]
target_1 = 22
target_2 = 0

nums_ceshi4 = [-4,-1,-1,0,1,1,2]
nums_ceshi3 = [-4,-1,-1,0,1,1,2]
nums_ceshi5 = []
nums_ceshi6 = [0]
nums_ceshi7 = [-1,1]
nums_ceshi8 = [-1,0,1]
nums_ceshi9 = [0,0,0,0,0,0,0]

solution = Solution()
# print(solution.twoSum(nums_ceshi1, target_1))
# print(solution.twoSum(nums_ceshi2, target_2))
# print(solution.twoSum(nums_ceshi4, 1))
print(solution.threeSum(nums_ceshi3))
print(solution.threeSum(nums_ceshi4))
print(solution.threeSum(nums_ceshi5))
print(solution.threeSum(nums_ceshi6))
print(solution.threeSum(nums_ceshi7))
print(solution.threeSum(nums_ceshi8))
print(solution.threeSum(nums_ceshi9))
