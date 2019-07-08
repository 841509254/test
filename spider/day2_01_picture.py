# -*- coding:utf-8 -*-

import urllib.request
import urllib.parse

from hlist import getheaders

url = "https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=2247692397,1189743173&fm=5"

req = urllib.request.Request(url,headers=getheaders())
res = urllib.request.urlopen(req)
html = res.read()
with open("maomi.jpg","wb") as f:
    f.write(html)
