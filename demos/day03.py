# 函数  字典


def f(name, age, **other):
    print("name=", name, "age=", age, "other=", other)


def fn(name, age, *other):
    print("name=", name, "age=", age, "other=", other)


def fnn(name, age=10, *other, **kwargs):
    print("name=", name, "age=", age, "other=", other, "**kwargs=", kwargs)


f("yangli", 88)
fn("yangli", 88)
f("yangli", 88, city="shanghai")
fn("yangli", 88, "shanghai")
fnn("yangli", 30, "jiangxi", "dongxiang", marrige="1", job="0", hobby="walking")

# 判断key是否在字典里
d = {"Bob": 99, "Yang": 30, "Kate": 12}
print(d)
# 使用in来判断key是否在指定的字典
if "Yang" in d:
    print("Yang YES")
else:
    print("Yang NO")

if "Bob" in d:
    print("Bob YES")
else:
    print("Bob NO")

# get到则返回key对应的value值，否则返回指定的值
print(d.get("Tomos", -1))
print(d.get("Yang", -1))
