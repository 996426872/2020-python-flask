"""
文件及目录
"""

print(os.getcwd())
print(os.listdir(r"C:\Users\hacker\Desktop\面试资料\1.SQLinuxNOSQL等\85-SQL必知必会"))

import os
from os import path
import glob

work_path = path.dirname (__file__)


def suffix(file , *suffixName):
    array = map (file.endswith , suffixName)
    if True in array:
        return True
    else:
        return False


def getFlist(path):
    lsdir = os.listdir (path)
    dirs = [i for i in lsdir if os.path.isdir (os.path.join (path , i))]
    if dirs:
        for i in dirs:
            getFlist (os.path.join (path , i))
    files = [i for i in lsdir if os.path.isfile (os.path.join (path , i))]
    for file in files:
        if suffix (file , ".bin" , ".ply"):
            os.remove (os.path.join (path , file))


getFlist(work_path)