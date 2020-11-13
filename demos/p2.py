import jieba

ls = jieba.lcut("中国是一个伟大的国家！")
print(ls)
ls1 = jieba.lcut("中国是一个伟大的国家！", cut_all=True)
print(ls1)

ls2 = jieba.cut_for_search("中华人民共和国是伟大的")
for i in ls2:
    print(i)