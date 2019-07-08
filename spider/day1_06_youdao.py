# -*- coding:utf-8 -*-

import urllib.request
import urllib.parse
import json

from hlist import getheaders

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
headers = getheaders()

key = input('请输入要翻译的内容：')

data={
    'i':key,
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':'15622344103543',
    'sign':'c56e4831704d908638eebe42549b080a',
    'ts':'1562234410354',
    'bv':'d675629694aa9348a06d778e004b8221',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_REALTlME',
}
data = urllib.parse.urlencode(data).encode("utf-8")
print(data)

req = urllib.request.Request(url,data=data,headers=headers)
res = urllib.request.urlopen(req)
html = res.read().decode('utf-8')
rdict = json.loads(html)

print(rdict)
print(rdict["translateResult"][0][0]["tgt"])
