# -*- coding = utf-8 -*-
# @Time : 2022/2/2 21:25
# @File : demo1.py
# @Software : PyCharm

"""
#格式化输出
age = 18
print("我的名字是%s，我的年龄是%d岁"%("小明",age))

#补充
print("aaa","bbb","ccc")
print("www","baidu","com",sep=".")
print("hello",end="")
print("world",end="\t")
print("python",end="\n")
print("end")

#输入
password = input("请输入密码：")
print("您刚刚输入的密码是：",password)
"""

# 一次性输入多个值
a, b = input("输入两个数，用空格隔开：").split()
print(a, b)
print("a的型是：%s，b的型是：%s" % (type(a), type(b)))
a, b = map(int, input("输入两个数，用空格隔开：").split())
print(a, b)
print("a的型是：%s，b的型是：%s" % (type(a), type(b)))
