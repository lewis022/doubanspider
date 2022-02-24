# -*- coding = utf-8 -*-
# @Time : 2022/2/15 16:24
# @Author : Hzj
# @File : testxlwt.py
# @Software : PyCharm

import xlwt

# workbook = xlwt.Workbook(encoding="utf-8")    # 创建workbook对象
# worksheet = workbook.add_sheet('sheet1')    # 创建工作表
# worksheet.write(0,0,"hello")    # 在第一行第一列写入数据“hello”，第一个参数为行，第二个参数为列，第三个参数为内容
# workbook.save('student.xlsx')    # 保存数据表到当前文件夹

# # 方法一：
# workbook = xlwt.Workbook(encoding="utf-8")
# worksheet = workbook.add_sheet('九九乘法表')
#
# # 输出99乘法表的列表
# list = []
# for a in range(1, 10):
#     for b in range(1, 10):
#         list.append(a * b)  # 将a*b的结果添加至列表
#
# # results = list
# # n = 9  # 每9个数换一行
# # for i in range(len(results)):
# #     print(results[i], end=' ')
# #     if (i+1) % 9 == 0:
# #         print(' ')
#
# # 为excel创建行列的乘数表头
# worksheet.write(0, 0, " ")
# f = 1
# h = 1
# for e in range(1, 10):
#     worksheet.write(0, e, f)
# for g in range(1, 10):
#     worksheet.write(g, 0, h)
#
# # 把之前列表的数依次填入excel表格内
# z = 0
# for x in range(1, 10):
#     for y in range(1, 10):
#         worksheet.write(x, y, list[z])
#         z = z + 1
#
# workbook.save('99乘法表.xlsx')


# 方法二（简便）：
workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet('99')

for i in range(0, 9):
    for j in range(0, i + 1):
        worksheet.write(i, j, "%d * %d = %d " % (i + 1, j + 1, (i + 1) * (j + 1)))

workbook.save('99.xlsx')
