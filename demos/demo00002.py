# 列表生成式
import os


# 简单办法，列表生成式
ks = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
ga = [i for i in ks if i > 0]
gm = [i for i in ks if i < 0]
print("大于零的数有{}个".format(len(ga)))
print("小于零的数有{}个".format(len(gm)))
# 传统办法，循环
a = 0
m = 0
for i in ks:
    if i > 0:
        a += 1
    if i < 0:
        m += 1
print("大于零的数有{}个".format(a))
print("小于零的数有{}个".format(m))



ls_file = [f for f in os.listdir("..")]
print(ls_file)

d = {"中国": "北京", "韩国": "首尔", "日本": "东京", "美国": "华盛顿"}
dg = [k+'的首都是'+v for k, v in d.items()]
print(dg)

kk = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
kkg = [i for i in kk if i % 2 == 0]
print(kkg)
