"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
你可以按任意顺序返回答案。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
说明:
返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

使用双指针的方式
时间复杂度O(n),空间复杂度O(1)

变化1：求出数组中所有满足的数组下标对或者值对，这种其实只是改变一点点判断条件，不改变算法主要流程
如果要求出所有的下标对，需要建立一个数组，找到一组就保存起来，直到左右指针相等；
同时修改下，找到一个不要return，左指针继续前进一步（或者右指针向左一步?）
数组有重复元素的时候要注意，注意下面的测试数据 nums_ceshi2
"""


class Solution:
    def twoSum(self, numbers, target):
        # 排序好的数组，左小右大
        # 和小于目标值，左指针右移动
        # 和大于目标值，右指针向左移动  直到找到满足条件的下标对或者左右两指针相等
        # 找到两数之和等于目标值，return两个下标

        i = 0
        j = len(numbers)-1
        while i < j:
            temp = numbers[i]+numbers[j]
            if temp == target:
                return [i, j]
            if temp > target:
                j = j - 1
            else:
                i = i + 1

        # 如果要求出所有的下标对，需要建立一个数组，找到一组就保存起来，直到左右指针相等；
        # 同时修改下，找到一个不要return，左指针继续前进一步（或者右指针向左一步?）
        # 数组有重复元素的时候要注意，注意下面的测试数据 nums_ceshi2
        # i = 0
        # j = len(numbers)-1
        # all = []
        # while i < j:
        #     temp = numbers[i]+numbers[j]
        #     if temp == target:
        #         all.append([i, j])
        #     if temp > target:
        #         j = j - 1
        #     else:
        #         i = i + 1
        # return all

# 看题目具体有哪些条件，设置正常的测试数据以及异常的测试数据
nums_ceshi1 = [2,7,11,11,15]
nums_ceshi2 = [-2,2,2,7,11,11,15]
target_1 = 22
target_2 = 0

solution = Solution()
print(solution.twoSum(nums_ceshi1, target_1))
print(solution.twoSum(nums_ceshi2, target_2))
