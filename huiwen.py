'''
返回字符串中最长回文
暴力破解方法
'''
# coding=utf8


s = "babadddd"
# t = "abcd"
# print(s[0:2:])
# 逆序访问数组
# print(t[::-1])
n = len(s)

final_ss = s[0]
final_len = 0
for i in range(0, n):
    for j in range(i+1, n):
        ss = s[i:j+1]
        print(ss)
        # 判断是否是回文，新回文是否大于已有回文长度，是就替换为最长回文
        if ss[::] == ss[::-1]:
            if len(ss) > final_len:
                print("产生新的回文串", ss)
                final_ss = ss
                final_len = len(ss)

# 输出列表s的最长回文子串
print("{}的最长回文串：{}".format(s, final_ss))


