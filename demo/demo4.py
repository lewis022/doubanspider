# -*- coding = utf-8 -*-
# @Time : 2022/2/2 23:15
# @File : demo4.py
# @Software : PyCharm

# 打印一条横线
def hx():
    print("------------------------")


print("hx输出开始", end="\n")
hx()
print("hx输出结束")
print()


# 可以通过输入的参数，打印自定义行数的横线
def hx_plus():
    a = int(input("请输入一个自然数："))
    for x in range(a):
        hx()


print("hx_plus输出开始", end="\n")
hx_plus()
print("hx_plus输出结束")
print()


# 求三数之和
def ssh(a, b, c):
    return a + b + c


a = float(input("请输入第一个数:"))
b = float(input("请输入第二个数:"))
c = float(input("请输入第三个数:"))
print("ssh输出开始", end="\n")
print(ssh(a, b, c))
print("ssh输出结束")
print()


# 求三数平均值
def sspjz(a, b, c):
    pjz = ssh(a, b, c) / 3
    return pjz


a = float(input("请输入第一个数:"))
b = float(input("请输入第二个数:"))
c = float(input("请输入第三个数:"))
print("sspjz输出开始", end="\n")
print(sspjz(a, b, c))
print("sspjz输出结束")
