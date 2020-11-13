# 私有成员


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_score(self):
        return self.__score

    def get_name(self):
        return self.__name

    def set_score(self, score):
        self.__score = score

    def set_name(self, name):
        self.__name = name


