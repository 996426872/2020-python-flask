"""
动态规划问题，递归问题
三角形最大路径和
保存计算过的最大路径和，可以将算法复杂度从2**n降低到n**2
"""
import time
max_sum_matrix = [[-1]*i for i in range(1, 101)]
tri = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
max_sum = 0


def dg_maxsum(row, column):
    global tri
    global max_sum
    global max_sum_matrix
    if max_sum_matrix[row][column] != -1:
        return max_sum_matrix[row][column]
    if row == (len(tri)-1):
        max_sum_matrix[row][column] = tri[row][column]
    else:
        max_sum_matrix[row][column] = max(dg_maxsum(row+1, column), dg_maxsum(row+1, column+1))+tri[row][column]
    return max_sum_matrix[row][column]


start_t = time.perf_counter()
print(dg_maxsum(0, 0))
end_t = time.perf_counter()
print("花费时间：{:.5f}".format(end_t-start_t))
