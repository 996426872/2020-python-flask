# 字符串 str() ord() chr() format()
print("{0:0>45d}".format(1))
xz = []
for i in range(0,12):
   xz.append(chr(9800+i))
print(xz)
xz_code = [ord(i) for i in xz]
print(xz_code)

sxh = []
for j in range(100, 1000):
    m = str(j)
    s = 0
    for i in m:
        s += eval(i)**3
    if s == j:
        sxh.append(j)
print(sxh)
sxh_str = ",".join([str(i) for i in sxh])
print(sxh_str)
print("出现7的次数为：", sxh_str.count("7"))
print(sxh_str.split(","))


