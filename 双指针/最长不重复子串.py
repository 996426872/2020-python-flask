"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        len_s = len(s)
        if len_s <= 1:
            return len_s
        start = 0
        end = 1
        # 最长串的左下标left，最长串为s[left:right:]
        left = 0
        right = 1
        s_dict = {}
        s_dict[s[0]] = 0
        # print(s_dict)
        while end < len_s:
            # print("s[{}]={}".format(end, s[end]))
            if s[end] not in s_dict:
                s_dict[s[end]] = end
                end = end + 1
                # print(s_dict)
                if end-start > right-left:
                    # 更新最长子串的左右下标
                    left = start
                    right = end
                # print(s[left:right],left,right)
            else:
                # 删除左指针start的元素（队列头pop出），右侧指针不变，直到重新变成不重复的子串为止
                del s_dict[s[start]]
                # print(s_dict)
                start = start + 1
        return right - left


solu = Solution()
str_test_zero = ""
str_test_one = "a"
str_test_n = "abcabcbb"
str_test_t = "pwwkew"
print(solu.lengthOfLongestSubstring(str_test_t))
print("-------------------------------------------")
