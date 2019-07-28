# -*- coding:utf-8 -*-
# import pymongo
# #
# # database = 'test'
# # table = 'test1'
# #
# # conn = pymongo.MongoClient('192.168.31.129',27017)
# #
# # db = conn[database]
# #
# # myset = db[table]
# #
# # myset.insert_one({'name':'lucy'})
# #
# # conn.close()
# # print('insert success')

# import  pymongo
#
# conn = pymongo.MongoClient('192.168.31.129',27017)
#
# dblist = conn.list_database_names()
# dbname = 'test'
# if dbname in dblist:
#     mydb = conn[dbname]
#     mycol = mydb['test1']
#     mycol.insert({'name':'jack','age':18,'sex':1},{'name':'nancy','age':22,'sex':2})
#
# conn.close()
# print('OK')

import time
import re
import urllib.request
import pymongo
from hlist import getheaders

class Maoyanspider(object):
    def __init__(self):
        self.baseurl = 'https://maoyan.com/board/4?offset='
        self.basere = 'class="movie-item-info".*?title="(.*?)".*?"star">\s+(.*?)\s+</p>.*?"releasetime">(.*?)</p>'
        self.conn = pymongo.MongoClient('192.168.31.129',27017)
        self.db = self.conn['maoyan']
        self.set = self.db['top100']

    def getHtml(self,url):
        req = urllib.request.Request(url,headers=getheaders())
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')
        return html

    def getRe(self,html):
        p = re.compile(self.basere,re.S)
        res = p.findall(html)
        return  res

    def mongoInsert(self,res):
        for r in res:
            d = {
                'name':r[0],
                'star':r[1],
                'relesetime':r[2]
            }
            self.set.insert_one(d)


    def workOn(self):
        for p in range(10):
            url = self.baseurl + str(p * 10)
            html = self.getHtml(url)
            r1 = self.getRe(html)
            self.mongoInsert(r1)
            print('第' + str(p + 1) + "页爬取成功！")
            time.sleep(1)
        self.conn.close()
        print('Success !')

if __name__ == '__main__':
    spider =Maoyanspider()
    spider.workOn()