# list.sort( key=None, reverse=False)
# 参数
# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
# 返回值
# 该方法没有返回值，但是会对列表的对象进行排序

# 已知一个队列[1, 3, 6, 9, 7, 3, 4, 6]
# 按从小到大排序
# 按从大大小排序
# 去除重复数字

aList = [1, 3, 6, 9, 7, 3, 4, 6]
bList = [1, 3, 6, 9, 7, 3, 4, 6]
aList.sort()
print(aList)
bList.sort(reverse=True)
print(bList)
print(list(set(bList)))

