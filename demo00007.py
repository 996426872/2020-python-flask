# 冒泡排序
a = [1, 3, 10, 9, 21, 35, 4, 6]
b = [7, 6, 5, 4, 3, 2, 1, 0]
jj = [i for i in range(1, len(b))]
jjs = jj[::-1]
print(jjs)

for j in jjs:
    print("第{}个数冒泡".format(j))
    for i in range(1, j+1):
        if b[i]<b[i-1]:
            k = b[i]
            b[i] = b[i-1]
            b[i-1] = k
    print(b)
