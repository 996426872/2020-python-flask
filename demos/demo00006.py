# 求完全数
qs = []
for q in range(1, 1000):
    q_yz = []
    q_sum = 0
    for i in range(1, q):
        if (q % i) == 0:
            q_yz.append(i)
    for k in q_yz:
        q_sum += k
    if q == q_sum:
        print("{}的因子是{}".format(q, q_yz))
        qs.append(q)
print("1000以内的完全数有", qs)




