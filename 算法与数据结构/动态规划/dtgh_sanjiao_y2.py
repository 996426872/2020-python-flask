"""
动态规划问题，递归问题
三角形最大路径和
保存计算过的最大路径和，可以将算法复杂度从2**n降低到n**2
将递归变成递推
"""
import time
max_sum_matrix = [[-1]*i for i in range(1, 101)]
tri = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]


def dg_maxsum(row, column):
    global tri
    global max_sum_matrix
    for i in range(0, len(tri)):
        max_sum_matrix[len(tri)-1][i] = tri[len(tri)-1][i]
    print(max_sum_matrix[len(tri)-1])
    li = [i for i in range(row, len(tri)-1)]
    li.reverse()
    print(li)
    for i in li:
        for j in range(0, i+1):
            print("i:", i, end=',')
            max_sum_matrix[i][j] = max(max_sum_matrix[i+1][j], max_sum_matrix[i+1][j+1])+tri[i][j]
            print("j:", j)
            print(max_sum_matrix[i][j])
    return max_sum_matrix[row][column]


start_t = time.perf_counter()
print(dg_maxsum(0,0))
end_t = time.perf_counter()
print("花费时间：{:.5f}".format(end_t-start_t))
