# -*- coding = utf-8 -*-
# @Time : 2022/2/2 22:03
# @File : demo2.py
# @Software : PyCharm

"""
f = open("test.txt", "w")  # 打开文件 w模式（写模式），文件不存在就新建
f.write("hello world,i am here!")  # 将字符串写入文件中
f.close()  # 关闭文件
"""

'''   #read方法，读取指定的字符，开始时定位在文件头部，每执行一次向后移动指定字符数
f = open("test.txt")
content = f.read(5)
print(content)
content = f.read(5)
print(content)
f.close()
'''

'''
f = open("test.txt")
content = f.readline()    # 读取一行字符，开始时定位在第一行，每执行一次向下移动一行
print(content)
content = f.readline()
print(content)
f.close()

f = open("test.txt")
content = f.readlines()    # 一次性读取全部文件为列表，每行一个字符串元素
print(content)
i = 1
for temp in content:
    print("%d:%s" % (i, temp))
    i += 1
f.close()
'''