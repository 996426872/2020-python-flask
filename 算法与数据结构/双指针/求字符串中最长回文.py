'''
返回字符串中最长回文子串
暴力破解方法
'''
# coding=utf8

class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        if n <= 1:
            print("特殊字符串")
            return s
        final_len = 0
        final_left = 0
        final_right = 0
        for i in range(0, n):
            for j in range(i+1, n):
                if j+1-i > final_len:
                    # up_s = s[i:j + 1:1]
                    # down_s = up_s[::-1]
                    # # print("正序", up_s)
                    # # print("逆序", down_s)
                    if self.isPalindrome(s[i:j + 1:1]):
                        final_left = i
                        final_right = j
                        final_len = j + 1 - i
                        # print("产生新的回文串", s[final_left:final_right+1:1])
        return s[final_left:final_right+1]

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

s = "cstgvkbrxacmpxdxxktktvpdzcuxmnhvuxdgsmskgeeawzeikhtmhdvnccbrgifpzmiuytfmeyfoxsntrdtxeuxcqsndexbgfxnthqwveujqzemloooyddparbjcuiwpopjwvvmwblsamkhjhlnoxinkpsempexmipifsfwzxbetgvfnkngzxcpizwctpdlpngjpyovmjllxfiwktghkxvyelwjwdztujmunijfsfdvmhgqhlpouewgyznphlmccjmqaqncwbeqheohibafqfunfywmrvqvjygjwqoclijwkcfiuaiymeagdbwyejnvtosxylptbtyoahfzfmwzrkhzdamknleroffmsqcaryibamgdpcumlhrblypddzhaxfeztokgogzgvpfvlmetiwsamhdidmvxavleryfyakendwrbslcavlqkerrnvpuzhdgwzuyorxzbkzhxhpbvkflgxouvaavxrdzsjlgrmogzvlhhdidldsxqhrqlryaanffhxnutcycnczuedtrwcnfiqrtoafvdfnfhxhyjivzalozrbrajboecfyalisxxanduzraqdrbzsbkobaieqpzcawrunxucypqyjnmrlrlivrrwwhdpekeelsphhunzbhkkejvqfopjsuholutgmtnleqdrntbqgrobnuhqpdkbjtikijkdiwqvnxgajaaqgswrdamzv"
solu = Solution()
print(solu.longestPalindrome(s))