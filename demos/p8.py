# 文件对象本身可迭代，而且是按行迭代, 不需要将文件所有行一次读取到列表中，尤其是大文件，读取不了的
# f = open("demo.txt", "r")
# ls = []
# lss = []
# for line in f:
#     ls = line.split(" ")
#     lss.append(ls)
# f.close
# print(lss)
#
# import sys
# print(sys.float_info)
# # 浮点数不确定尾数问题，来源于计算机二进制无法精准表示出自然小数
# print(0.1+0.2)
# print(round(0.1+0.2, 1))
#
#
# print(",".join("1234567"))
# ll = ["hello", "world", "good day"]
# print(" ".join(ll))
# print(",".join(ll))
def feb(n):
    if n == 1 or n == 2:
        return 1
    else:
        return feb(n-1)+feb(n-2)


# print(feb(1))
# print(feb(2))
# print(feb(3))
# print(feb(4))
# print(feb(5))
# print(feb(6))
# print(feb(7))
# print(feb(8))
# print(feb(9))
# print(feb(10))

# for n in range(10):
#     print(feb(n))

# 对集合进行减运算，得到集合间的差集
A = {'p', 'y', 123}
B = set('pypy123')
print(B)
print(A-B)
print(B-A)

print(A&B)
print(A|B)
print(A^B)