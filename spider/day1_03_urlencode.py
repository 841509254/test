# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse


headers = {"User-Agent":""}
#baseurl = "http://www.baidu.com/s?"
baseurl = "http://www.baidu.com/s?wd="

val = input("请输入要搜索的内容")
# key = urllib.parse.urlencode({"wd":val})
key = urllib.parse.quote(val)
url = baseurl + key

req = urllib.request.Request(url,headers=headers)
res = urllib.request.urlopen(req)
html = res.read().decode("utf-8")

with open('百度.html','w',encoding='utf-8') as f:
    f.write(html)
print("Success!")