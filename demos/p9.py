# 数据清洗
try:
    f = open("university.txt", 'r', encoding="utf-8")
    ls = []
    for line in f:
        if "alt" in line:
            toks = line.split('"')
            print(toks)
            uname = toks[-2]
            if "大学生" in uname or "MOOC" in uname:
                continue
            if "大学" in uname or "学院" in uname:
                ls.append(uname)
    ls.sort()
    print(", ".join(ls))
    print(len(ls))
except:
    print("文件打开错误")
finally:
    f.close()
