# -*- coding = utf-8 -*-
# @Time : 2022/2/8 23:42
# @File : testre.py
# @Software : PyCharm


# 正则表达式：字符串模式（判断字符串是否符合一定的标准）

import re

# 创建模式对象

pat = re.compile("AA")  # 此处的AA是正则表达式，用于去验证其他的字符串
# m = pat.search("CBA")     # search字符串被校验的内容
# m = pat.search("ABCAA")
# m = pat.search("AABCAADDCCAAA")    # search方法，进行比对查找

# 没有模式对象

# m = re.search("asd", "Aasd")  # 前面的字符串是规则，后面的字符串是被校验的对象

# m = re.findall("[A-Z]", "ASDaDFGAa")    # 前面的字符串是规则（正则表达式），后面的字符串是被校验的对象

# m = re.findall("[A-Z]+", "ASDaDFGAa")

# sub

# m = re.sub("a", "A", "abcdcasd")       # 找到a用A替换，在第三个字符串中查找

# print(m)

# 建议在正则表达式中，被比较的字符串前面加上r，为了不用担心转义字符的问题

# a = r"\aabd-\'"

# print(a)


