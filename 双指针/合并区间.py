"""
给出一个区间的集合，请合并所有重叠的区间。

 

示例 1:

输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:v c

输入: intervals = [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

排序+双指针 解决这类问题

"""
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/merge-intervals/solution/he-bing-qu-jian-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


?????输入不是数组，是链表

"""


class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals,key=lambda x:x[0])
        # 初始化 待合并的前区间 指向要处理的区间index
        pre_inter = intervals[0]
        index = 1
        while index<len(intervals):
            if intervals[index][0]>pre_inter[1]:
                # 如果待处理的区间左边界大于待合并的前区间的右边界，两区域无重叠，index+=1
                pre_inter = intervals[index]
                index = index + 1
            else:
                # 合并两个区间
                # inter = [pre_inter[0],max(pre_inter[1],intervals[index][1])]
                pre_inter[1] = max(pre_inter[1],intervals[index][1])
                del intervals[index]
        return intervals


if __name__ == "__main__":
    intervals = [[1,4],[4,5]]
    solu = Solution()
    print(solu.merge(intervals))

    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # solu = Solution()
    print(solu.merge(intervals))


    intervals = [[1 , 3]]
    # solu = Solution()
    print(solu.merge(intervals))


    intervals = [ [15 , 18],[8 , 10],[2,6],[1,3]]
    solu = Solution()
    print(solu.merge(intervals))