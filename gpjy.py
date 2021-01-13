"""
股票交易最大收益
不限制次数
限制2次
"""
class Solution:
    def maxProfit(self, prices):
        # p_list = []
        max_p = 0
        max_1_p = 0
        max_2_p = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
               max_p = max_p + prices[i] - prices[i-1]
               if i == len(prices)-1:
                   # p_list.append(max_p)
                   if max_p > max_1_p:
                        max_2_p = max_1_p
                        max_1_p = max_p
                   else:
                       max_2_p = max(max_2_p,max_p)
                   # print (max_1_p)
                   # print (max_2_p)
                   # print (p_list)
            else:
                if max_p != 0:
                    if max_p > max_1_p:
                        max_2_p = max_1_p
                        max_1_p = max_p
                    else:
                        max_2_p = max(max_2_p, max_p)
                    # p_list.append(max_p)
                    # print (max_1_p)
                    # print (max_2_p)
                    # print (p_list)
                    max_p = 0
        return max_1_p+max_2_p

s = Solution()
ceshi1 = [51,90,28,59,76,47,9,39,3,96,36,31,81,6,45,46,78,94,27,89,20,66,76,94,27,77,70,51,99,81,88,44,54,73,7,80,53,39,15,26,88,22,54,50,76,61,10,8,57,36,28,47,32,7,79,75,86,28,19,23,9,75,32,88,59,33,2,56,21,69,74,46,78,27,92,26,88,14,22,11,46,11,1,8,62,52,91,64,21,53,69,33,69,22,90,10,58,20,79,7]
max = s.maxProfit(ceshi1)
print(max)


# class Solution:
#     def maxProfit(self, prices):
#         p_list = []
#         max_p = 0
#         max_1_p = 0
#         max_2_p = 0
#         for i in range(1, len(prices)):
#             if prices[i] > prices[i-1]:
#                max_p = max_p+prices[i] - prices[i-1]
#                if max_p > max_1_p:
#                    max_2_p = max_1_p
#                    max_1_p = max_p
#                else:
#                    max_2_p = max(max_2_p, max_p)
#         return max_1_p,max_2_p
#
# s = Solution()
# max_1_p,max_2_p = s.maxProfit([8,9,10,11])
# print(max_1_p)
# print(max_2_p)
