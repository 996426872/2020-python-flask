# 序列操作

# creature = "cat", "dog", "tiger", "human"
# print(creature[::-1])
# # 创建了一个新的逆序元组，没改变creature
# color = 0x001100, "blue", creature
# print(color)
# print(color[-1][2])


d1 = {}
d1['a'] = 1
d1['b'] = 2
print(list(d1.keys()))
et = 'c' in d1.keys()
print(et)
#
# print(d1.popitem())
# print(d1.keys())
print(list(d1.items()))