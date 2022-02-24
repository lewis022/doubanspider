# -*- coding = utf-8 -*-
# @Time : 2022/2/15 17:47
# @Author : Hzj
# @File : testSqlite.py
# @Software : PyCharm

import sqlite3

# # 1、链接数据库
# conn = sqlite3.connect("test.db")    # 打开或创建数据库文件
# print("成功打开数据库")


# # 2、创建数据表
# conn = sqlite3.connect("test.db")    # 打开或创建数据库文件
# print("成功打开数据库")
#
# c = conn.cursor()     # 获取游标
#
# sql = '''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real);
# '''
#
# c.execute(sql)    # 执行sql语句
# conn.commit()    # 提交数据库操作
# conn.close()    # 关闭数据库链接
# print("成功建表")


# # 3、插入数据
# conn = sqlite3.connect("test.db")    # 打开或创建数据库文件
# print("成功打开数据库")
#
# c = conn.cursor()     # 获取游标
#
# sql1 = '''
#     insert into company (id,address,age,name,salary)
#     values(1,"成都",32,"张三",8000);
# '''
#
# sql2 = '''
#     insert into company (id,address,age,name,salary)
#     values(2,"重庆",30,"李四",10000);
# '''
# c.execute(sql1)    # 执行sql语句
# c.execute(sql2)
# conn.commit()    # 提交数据库操作
# conn.close()    # 关闭数据库链接
# print("插入数据完毕")


# # 4、查询数据
#
# conn = sqlite3.connect("test.db")    # 打开或创建数据库文件
# print("成功打开数据库")
#
# c = conn.cursor()     # 获取游标
#
# sql = '''
#     select * from company
# '''
#
# cursor = c.execute(sql)
#
# for row in cursor:
#     print("id= ", row[0])
#     print("name= ", row[1])
#     print("age= ", row[2])
#     print("address= ", row[3])
#     print("salary= ", row[4], end="\n\n")
#
# conn.close()    # 关闭数据库链接
# print("查询完毕")

conn = sqlite3.connect("test.db")    # 打开或创建数据库文件
print("成功打开数据库")

c = conn.cursor()     # 获取游标

# sql = '''
#     create table movie250(
#     id integer primary key autoincrement,
#     info_link text,
#     pic_link text,
#     cname varchar,
#     ename varchar,
#     score numeric,
#     rated numeric,
#     introduction text,
#     info text)
# '''

# sql = 'drop table movie250'

sql = '''
    insert into movie250( 
    info_link,pic_link,cname,ename,score,rated,introduction,info) 
    values(
    "https://movie.douban.com/subject/2297265/",
    "https://img2.doubanio.com/view/photo/s_ratio_poster/public/p1344888983.jpg",
    "浪潮",
    "Die Welle",
    "8.7",
    "243630",
    "世界离独裁只有五天",
    "导演: 丹尼斯·甘塞尔 Dennis Gansel   主演: 尤尔根·沃格尔 Jürgen Vogel ... 2008 / 德国 / 剧情 惊悚") 
'''

c.execute(sql)    # 执行sql语句
conn.commit()    # 提交数据库操作
conn.close()    # 关闭数据库链接
print("成功操作")