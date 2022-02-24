# -*- coding = utf-8 -*-
# @Time : 2022/2/3 23:41
# @File : testurllib.py
# @Software : PyCharm

import urllib.request
import urllib.parse

# # 获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))  # 对获取到的网页源码用utf-8来解码

# # 获取一个post请求
# data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post", data=data)
# print(response.read().decode('utf-8'))

# # 超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("time out")

# # 补充
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))    # 网页源码
# print(response.status)    # 状态码
# print(response.getheaders())     # 响应头
# print(response.getheader("Server"))    # 只读server

# # 封装headers
# url = "http://httpbin.org/post"
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                          "Chrome/98.0.4758.82 Safari/537.36"}
# data = bytes(urllib.parse.urlencode({"name": "eric"}), encoding="utf-8")
# req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

# 访问豆瓣
url = "http://www.douban.com"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/98.0.4758.82 Safari/537.36"}
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
