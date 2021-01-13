class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)-1
        i=0
        j=n
        flag = True
        while i < j:
            if s[i] != s[j]:
                flag = False
                break
            i = i + 1
            j = j - 1
        return flag


def clear_str(raw_s):
    ts = ""
    for i in raw_s.lower():
        if i.isalnum() or i.isalpha():
            ts = ts + i
            print("ts处理:", ts)
    return ts


s = Solution()
t = "ab c,1-1?1c_ba"
print("{}是回文串：{}".format(t, s.isPalindrome(clear_str(t))))
