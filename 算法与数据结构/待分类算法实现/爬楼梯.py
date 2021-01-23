"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def climbStairs(self, n):
        a = 1
        b = 1
        for i in range(1,n+1):
            # print("爬{}个台阶有{}种方法".format(i,b))
            a, b = b, a+b
        return a


if __name__ == "__main__":
    test_jieti1 = 0
    test_jieti2 = 1
    test_jieti3 = 2
    test_jieti4 = 3
    test_jieti5 = 4
    solu = Solution()
    print(solu.climbStairs(test_jieti1))
    print (solu.climbStairs(test_jieti2))
    print (solu.climbStairs(test_jieti3))
    print (solu.climbStairs(test_jieti4))
    print (solu.climbStairs (test_jieti5))