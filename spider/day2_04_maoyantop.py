# -*- coding:utf-8 -*-

import time
import re
import csv
import urllib.request

from hlist import getheaders

class Maoyanspider(object):
    def __init__(self):
        self.baseurl = 'https://maoyan.com/board/4?offset='
        self.basere = 'class="movie-item-info".*?title="(.*?)".*?"star">\s+(.*?)\s+</p>.*?"releasetime">(.*?)</p>'
        self.filename = '猫眼电影top100.csv'

    def getPage(self,url):
        req = urllib.request.Request(url,headers=getheaders())
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
        return html

    def getRe(self,html):
        p = re.compile(self.basere,re.S)
        r1 = p.findall(html)
        return r1

    def writeInfo(self,r1):
        with open(self.filename,'a',newline='') as f:
            writer = csv.writer(f)
            for r in r1:
                writer.writerow(r)


    def workOn(self):
        with open(self.filename, 'w', newline='') as f:
            f.write('')
        for p in range(10):
            url = self.baseurl + str(p*10)
            html = self.getPage(url)
            r1 = self.getRe(html)
            self.writeInfo(r1)
            print('第' + str(p + 1) + "页爬取成功！")
            time.sleep(1)
        print('Success !')

if __name__ == '__main__':
    spider = Maoyanspider()
    spider.workOn()


