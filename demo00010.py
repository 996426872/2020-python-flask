"""
构造和析构函数
实例对象的引用
Version: 1.0
Author: 杨黎
"""
# coding=utf8
import sys


class DemoClass:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        return len(self.name)

    def __del__(self):
        print("再见，{}".format(self.name))


doc1 = DemoClass("老王")
doc2 = doc1
print(sys.getrefcount(doc1))
del doc1
print(doc2.name)
