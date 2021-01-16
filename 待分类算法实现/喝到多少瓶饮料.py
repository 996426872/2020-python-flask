"""
输入例子1:
3
10
81
0

输出例子1:
1
5
40
"""

def get_bottles(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    sum_bottles = 0
    while n>=3:
        sum_bottles = sum_bottles + (n//3)
        kong_bottles = n//3 + n%3
        n = kong_bottles
    if n==2:
        sum_bottles = sum_bottles +1
    return sum_bottles

while True:
    n = int(input())
    if n == 0:
        break
    print(get_bottles(n))