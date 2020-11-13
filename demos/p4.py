
# dayUp = 1.0
# dayFactor = 0.01
# for i in range(365):
#     if i % 7 in [0, 6]:
#         dayUp = (1.0 - dayFactor)*dayUp
#     else:
#         dayUp = (1.0 + dayFactor)*dayUp
# print("工作日的力量：{:.2f}".format(dayUp))


def du(df, *d):
    dayup = 1.0
    dayfactor = df
    for i in range(365):
        if i % 7 in d:
            dayup  = (1.0 - dayfactor) * dayup
        else:
            dayup  = (1.0 + dayfactor) * dayup
    if len(d) == 0:
        xiuxi = "NO"
    else:
        xiuxi = "YES"
    print("天天向上的力量：每天努力{:.3f}，结果{:.3f}，休息:{}".format(dayfactor, dayup, xiuxi))
    return dayup


# du(0.001)
# du(0.005)
du(0.01)
du(0.025, 0, 6)

re = du(0.01)
dayfactor = 0.01
re1 = 0
while re1<re:
    dayfactor += 0.001
    re1 = du(dayfactor, 0, 6)
