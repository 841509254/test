# -*- coding:utf-8 -*-

import csv

with open("test.csv",'w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['小姐姐','20'])
    writer.writerow(('小哥哥', '25'))
