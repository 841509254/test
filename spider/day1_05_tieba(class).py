# -*- coding:utf-8 -*-

import time
import urllib.request
import urllib.parse

from hlist import getheaders

class Baiduspider(object):
    def __init__(self):
        self.baseurl = "https://tieba.baidu.com/f?"

    def getPage(self,url):
        req = urllib.request.Request(url,headers=getheaders())
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
        return html

    def parsePage(self):
        pass

    def writePage(self,filename,html):
        with open(filename,'w',encoding='utf-8')as f:
            f.write(html)

    def workOn(self):
        name = input("请输入你要爬取的贴吧：")
        start = int(input("请输入爬取起始页："))
        end = int(input("请输入爬取结束页："))
        for p in range (start,end+1):
            page = (p-1)*50
            key = urllib.parse.urlencode({"kw":name,"pn":page})
            url = self.baseurl + key
            print(url)
            filename = name + "吧第" + str(p) + "页.html"
            html = self.getPage(url)
            self.writePage(filename,html)
            print(filename+"爬取成功")


if __name__ == '__main__':
    start = time.time()
    spider = Baiduspider()
    spider.workOn()
    end = time.time()
    print("执行时间 %.2f" % (end - start))