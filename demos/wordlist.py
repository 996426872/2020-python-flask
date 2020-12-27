import yaml


def add_word():
    word = input("请输入你要添加的单词")
    if word in word_dic.keys():
        print("你输入的单词已经存在")
    else:
        word_meaning = input("请输入单词的词义")
        word_dic[word] = word_meaning
        print("单词添加成功")
        print("最新的单词本为：", word_dic)


def query_word():
    word = input("请输入你查询的单词")
    if word in word_dic.keys():
        print("您查询的单词存在，单词的含义为", word_dic[word])
        print("最新的单词本为：", word_dic)
    else:
        print("很抱歉，查询不到您要查找的单词")


def delete_word():
    word = input("请输入你删除的单词")
    if word in word_dic.keys():
        print("您要删除的单词存在，单词的含义为", word_dic[word])
        del word_dic[word]
        print("单词删除成功")
        print("最新的单词本为：", word_dic)
    else:
        print("很抱歉，查询不到您要删除的单词")


if __name__ == "__main__":
    # 加载文件内容，初始化字典
    word_dic = {}
    with open("words.yml", "r") as f:
        word_dic = yaml.safe_load(f)

    while True:
        command = input("欢迎使用单词本，请输入命令：添加1，查询2，删除3，退出4:")
        if command == "1":
            add_word()
        if command == "2":
            query_word()
        if command == "3":
            delete_word()
        if command == "4":
            print("谢谢使用！")
            break
    # 退出前写入文件
    with open("words.yml", "w") as f:
        yaml.dump(word_dic, f)

