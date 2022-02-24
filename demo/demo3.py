# -*- coding = utf-8 -*-
# @Time : 2022/2/2 22:37
# @File : demo3.py
# @Software : PyCharm

"""
# 捕获异常
try:
    print("-------1--------")
    f = open("123.txt")  # 默认只读打开了一个不存在的文件，报错
    print("-------2--------")  # 报错，故没有执行
except IOError:  # 文件没有找到，属于IO异常（输入输出异常）
    pass  # 捕获异常后，执行的代码
"""

"""
# 获取错误描述
try:
    print("-------1--------")
    f = open("123.txt")  # 默认只读打开了一个不存在的文件，报错
    print("-------2--------")  # 报错，故没有执行
except (IOError, NameError) as result:  # 文件没有找到，属于IO异常（输入输出异常）
    print(result)
"""

"""
#捕获所有异常
try:
    print("-------1--------")
    f = open("123.txt")
    print("-------2--------")
except Exception as result:  # Exception可以承接所有异常
    print(result)
"""

"""
# try......finally 和嵌套 重点
import time

try:
    f = open("test.txt")
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print("文件关闭")
except Exception as result:
    print("发生异常")
"""