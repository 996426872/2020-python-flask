# 冒泡排序
a = [1, 3, 10, 9, 21, 35, 4, 6]
b = [7, 6, 5, 4, 3, 2, 1, 0]



def bubble(li):
    print("待排序序列", li)
    # 交换次数
    jjs = range(1, len(li))[::-1]
    print(jjs)

    for j in jjs:
        print("第{}位置数冒泡".format(j))
        for i in range(0, j):
            if li[i] > li[i+1]:
                li[i+1], li[i] = li[i], li[i+1]
        print(li)


bubble(a)
bubble(b)
