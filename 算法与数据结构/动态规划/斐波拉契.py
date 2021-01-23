"""
下面f(0)是斐波拉契数列第一位，先这样定

实际上调用 fib(n)时，调用次数不该超过 O(n)。原因很简单，在调用 fib 时所有可能的值
一共也就 O(n)个。我们只需缓存每次计算 fib(i)的结果，以备后续使用。
这也是称其为记忆法的原因所在。
只要对上面的函数稍作修改，就可以

1.简单的递归方式，耗时O(2**n),feb1(n)；
2.自上而下的记忆法，耗时很短feb(n, memo)，借助少量的空间，换取更快的时间是非常划算的；
3.自下而上的递推方法，耗时很短feb2(n),需要借助的空间也更少；

"""
import time

# memo数组记忆feb结果
def feb(n, memo):
    if n == 0 or n == 1:
        memo[n] = 1
        # print("memo[{}]={}".format (n , memo[n]))
        return 1
    if memo[n] == -1:
        memo[n] = feb(n-1, memo) + feb(n-2, memo)
        # print("memo[{}]={}".format(n, memo[n]))
    return memo[n]

# 递归
def feb1(n):
    if n == 0 or n == 1:
        return 1
    return feb1(n-1) + feb1(n-2)


def feb2(n):
    if n == 0 or n == 1:
        return 1
    a = 1
    b = 1
    for i in range(2, n+1):
        a, b = b, a+b
    return b


n = 400
memo_febs = [(-1) for i in range(n+1)]
# print(memo_febs)
start = time.time()
print(start)
# print(feb(n, memo_febs))284812298108489611757988937681460995615380088782304890986477195645969271404032323901
# print(feb1(n))
# print(memo_febs)
print(feb2(n))
end = time.time()
print(end)
print(end-start)

