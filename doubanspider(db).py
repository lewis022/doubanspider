# -*- coding = utf-8 -*-
# @Time : 2022/2/3 23:03
# @File : doubanspider.py
# @Software : PyCharm

from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt
import sqlite3


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1、爬取网页
    datalist = getData(baseurl)
    # 2、解析数据（逐一解析数据）
    # 3、保存数据
    dbpath = "movie.db"  # 保存在当前文件夹用“.”
    saveData2DB(datalist, dbpath)


# 影片详情页链接的规则
findlink = re.compile(r'<a href="(.*?)">')  # 创建正则表达式对象，表示规则（字符串的模式）  # 这个为全局变量    # 影片超链接的规则    # () 表示捕获分组，()
# 会把每个分组里的匹配的值保存起来，多个匹配值可以通过数字 n 来查看(n 是一个数字，表示第 n 个捕获组的内容)
# 影片图片的规则
findImgSrc = re.compile(r'<img.*src="(.*?)" width="100"/>', re.S)  # re.S 让换行符包含在字符中
# 影片片名的规则
findTitle = re.compile(r'<span class="title">(.*?)</span>', re.S)
# 影片评分的规则
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>', re.S)
# 评价人数的规则
findJudge = re.compile(r'<span>(.*?)人评价</span>')
# 概况的规则
findInq = re.compile(r'<span class="inq">(.*?)</span>')
# 找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 爬取网页
def getData(baseurl):
    datalist = []

    for i in range(0, 10):  # 调用获取页面信息的函数10次
        url = baseurl + str(i * 25)
        html = askURL(url)  # 保存获取到的网页源码
        # 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):  # 查找符合要求的字符串，形成列表
            # print(item)    # 测试查看电影item全部信息
            data = []  # 保存一部电影的所有信息
            item = str(item)

            link = re.findall(findlink, item)[0]  # re库通过正则表达式用来查找指定字符串    # [0]表示如果得到的是个列表，则拿到第一个元素
            data.append(link)  # 添加链接到数据库

            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)  # 添加图片到数据库，以下同理

            title = re.findall(findTitle, item)  # 片名可能只有一个名字（中文名），没有别名（外国名）
            if len(title) == 2:
                ctitle = title[0]
                data.append(ctitle)  # 添加中文名
                otitle = title[1].replace("/", "")  # 去掉无关的符号
                data.append(otitle.strip())  # 添加外国名
            else:
                data.append(title[0])
                data.append("")  # 外国名留空

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)

            inq = re.findall(findInq, item)  # 这里需要判断如果列表为null的情况
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
                data.append(inq.strip())
            else:
                data.append("")

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)  # 去掉<br/>
            data.append(bd.strip())  # strpe()为去掉前后的空格
            datalist.append(data)  # 把处理好的一切电影信息放入datalist

    return datalist


# 得到指定一个URL的网页内容
def askURL(url):
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/98.0.4758.82 Safari/537.36"}
    # 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接受什么水平的文件）
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)    # 测试查看网页源码
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 保存数据
def saveData2DB(datalist, dbpath):
    print("saving...")
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            data[index] = '"' + data[index] + '"'
            # noinspection SpellCheckingInspection
        sql = '''
            insert into movie250(
            info_link,pic_link,cname,ename,score,rated,introduction,info)
            values(%s)
        ''' % ",".join(data)  # {",".join(data)} 表示把data列表每个中间用“,”链接
        # print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


# 创建数据库
def init_db(dbpath):
    sql = '''
        create table movie250
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric,
        rated numeric,
        introduction text,
        info text
        )
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    main()
    # init_db("movie.db")    # 测试是否创建了数据库
    print("爬取完毕！")
