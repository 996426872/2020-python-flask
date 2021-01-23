"""
双指针解法
"""


class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        if n <= 0:
            return n

        print("处理前nums:", nums)
        print("------------------------------------")
        # 初始化待处理的可能会重复的字符 a = nums[0]
        a = nums[0]
        # 初始化，处理的字符下标
        index = 1
        while index < len(nums):
            if nums[index] == a:
                del nums[index]
                print("删除字符:", a)
                print("删除字符后，数组后面元素全部向前挪动一位了，数组是：", nums)
                print("待处理的字符和待处理的数组下标都不会发生变化")
            else:
                print("已经处理字符是：", a)
                print("已经处理数组下标是：", index)
                a = nums[index]
                index = index + 1
                print("当前字符已经和之前的不一样，作为下一个待处理字符是：", a)
                print("要处理数组下标向右挪动一位，是：", index)
            print("------------------------------")
        return len(nums)


if __name__ == "__main__":
    solu = Solution()
    print(solu.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
