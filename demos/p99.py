f = open("writelinetest.txt", "w+", encoding="utf-8")
ll = ["美国", "中国", "日本", "韩国", "俄罗斯"]
f.writelines(ll)
f.seek(0)
for line in f:
    print(line)
