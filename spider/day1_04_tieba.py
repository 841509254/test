# -*- coding:utf-8 -*-
import random
import time

import urllib.request
import urllib.parse

from hlist import getheaders

headers = getheaders()
baseurl = "https://tieba.baidu.com/f?"

name = input("请输入你想爬取的贴吧名：")
begin = int(input("请输入你想爬取的起始页："))
end = int(input("请输入你想爬取的终止页："))

for p in range(begin,end+1):
    page = (p-1)*50
    key = urllib.parse.urlencode({"kw":name,"pn":page})
    print(key)
    url = baseurl + key
    print(url)
    req = urllib.request.Request(url,headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read().decode("utf-8")
    filename = name + '吧第' + str(p) + '页.html'
    with open(filename,"w",encoding="utf-8") as f:
        f.write(html)
        print(filename+"爬取成功")
    time.sleep(0.5)

print("success!")
