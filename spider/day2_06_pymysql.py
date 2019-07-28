# -*- coding:uff-8 -*-

import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='123456',
                     database='db5',
                     charset='utf8')

cur =db.cursor