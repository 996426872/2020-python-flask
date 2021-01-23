"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def maxProfit(self, prices):
        maxProfit = 0
        if len(prices) < 2:
            return maxProfit
        # 调试用代码，记录当前一次买入和卖出的价格
        # minPrice = prices[0]
        # maxPrice = prices[1]
        # print("maxPrice:", maxPrice , end=',')
        # print("minPrice:", minPrice)
        for i in range(1, len(prices)):
            # 如果今天股价大于昨天股价，则默认昨天是买入，今天是卖出，获取到这个差额利润
            if prices[i] > prices[i-1]:
                maxProfit = maxProfit + prices[i] - prices[i-1]
            #     maxPrice = prices[i]
            # else:
            #     minPrice = prices[i]
            # print("i:", i, end=',')
            # print("maxProfit:", maxProfit, end=',')
            # print("maxPrice:", maxPrice, end=',')
            # print("minPrice:", minPrice)
        return maxProfit


# 调试代码，输入测试数据

    prices = [7,1,5,3,6,4]
    prices_ceshi = [7,1,5,7,3,6,6,6,8,4]
    solu = Solution()
    print("测试普通数据-----------------------", prices)
    print(solu.maxProfit(prices))
    print("测试有相同股价时-----------------------", prices_ceshi)
    print(solu.maxProfit(prices_ceshi))
