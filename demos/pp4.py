# 生成器generator类 可迭代对象
from collections.abc import Iterable,Iterator

g = (x*x for x in range(10001))
# print(next(g))
# for n in g:
#     print(n)

print(isinstance(g, Iterable))
print(isinstance(g, Iterator))
