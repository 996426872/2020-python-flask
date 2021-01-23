"""
求最大子串的和
返回最大子串的和
"""
class Solution:
    def maxsumofSubarray(self, arr):
        num_sum = arr[0]
        max_sum = num_sum
        for i in range(1, len(arr)):
            print("arr[i]=", arr[i])
            if num_sum > 0:
                num_sum += arr[i]
            else:
                num_sum = 0+arr[i]
            max_sum = max(max_sum, num_sum)
            print("num_sum", num_sum)
            print("max_sum", max_sum)
        return max_sum

s = Solution()
print(s.maxsumofSubarray([-2, 3, 5, -2, 6, -1]))