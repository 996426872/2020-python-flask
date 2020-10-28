from functools import reduce
# 高阶函数，map，reduce
"""map()函数接收两个参数，一个是函数，一个是Iterable，
map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。"""

"""reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)"""


def normalize(name):
    return name.title()


def add(x,y):
    return 10*x+y


print(normalize("aBcghhjDGH"))
print(add(1, 2))

L = ['adam', 'LISA', 'barT']
LL = map(normalize, L)
print(L)
print(list(LL))

ar = [8, 4, 3, 9, 2]
ars = reduce(add, ar)
print(ars)



