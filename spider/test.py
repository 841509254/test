# -*- coding:utf-8 -*-

import random
import time

# import re
# #
# # s = "A B C D"
# #
# # p = re.compile("(\w+)\s+\w+\s+(\w+)")
# # r1 = p.findall(s)
# #
# # print(r1)

# s = 'hcccccccaaaabbbbeeffgddddd'
#
#
# def remove_most(s):
#     l=[]
#     for x in s:
#         if (x,s.count(x)) not in l:
#             l.append((x,s.count(x)))
#     l1=sorted(l,key=lambda x :x[1],reverse=True)
#     s = s.replace(l1[0][0],'')
#     return s,l1
#
# if __name__ == '__main__':
#     s1,l1= remove_most(s)
#     print(s1,l1,sep='\n')


# 冒泡排序\

# def my_bubble(l):
#     start = time.time()
#     count = 0
#     for x in range(len(l)-1):
#         # flag = True
#         for y in range(len(l)-1-x):
#             count += 1
#             if l[y] > l[y+1]:
#                 l[y],l[y+1] = l[y+1],l[y]
#         #         flag = False
#         # if flag:
#         #     break
#     end = time.time()
#     print(count)
#     return l,end-start
#
# t = []
# for z in range(10):
#     l = []
#     for x in range(1501):
#         l.append(random.randint(1, 10000))
#         # l = sorted(l)
#     l,ti = my_bubble(l)
#     t.append(ti)
# print(l,t,sum(t))


# 冒泡排序
# def my_bubble(l):
#     for x in range(len(l)-1):
#         for y in range(len(l)-1-x):
#             if l[y] > l[y+1]:
#                 l[y],l[y+1] = l[y+1],l[y]
#     return l
#
# l=[]
# for x in range(101):
#     l.append(random.randint(1,9999))
# print(my_bubble(l))

def dec(fn):
    def fx(x,y):
        print('两者中较大的是：')
        print(fn(x,y))
    return fx

@dec
def my_max(x,y):
    return x if x>y else y

my_max(3,8)