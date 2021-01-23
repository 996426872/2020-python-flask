"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxSubArray(self, nums):
        nums_sum = nums[0]
        max_nums_sum = nums[0]
        for i in range(1,len(nums)):
            if nums_sum<0:
                nums_sum = nums[i]
            else:
                nums_sum = nums_sum + nums[i]
            max_nums_sum = max(max_nums_sum, nums_sum)
        return max_nums_sum


if __name__ == "__main__":
    solu = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(solu.maxSubArray(nums))



