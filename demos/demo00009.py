# coding=utf8
"""
map/reduce 递归
Version: 1.0
Author: 杨黎
"""
from functools import reduce


def f(x):
    return x * x


def fn(x, y):
    return x * y


a = [1, 2, 3, 4]
t = map(f, a)
print("map对列表求f(x)=x*x")
for i in t:
    print(i, end=' ')
print()

# 求阶乘n!
k = 10
print("reduce求解{}!={}".format(k, reduce(fn, range(1, k + 1))))


def fr(n):
    if n == 1:
        return 1
    else:
        return n*fr(n-1)


print("递归求解阶乘{}!={}".format(3, fr(3)))
print("递归求解阶乘{}!={}".format(10, fr(10)))


