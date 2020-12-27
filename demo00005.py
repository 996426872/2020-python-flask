# 序列
# 问题：将第一个元素放到第三个位置
ls = [1, 3, 5, 7]
# ls_new = ls[1:4]
# ls_new[1:2] = [5, 1]
# print(ls_new)
# print(ls.pop(0))
ls.insert(2, ls.pop(0))
print(ls)