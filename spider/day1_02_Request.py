#! coding=utf-8
import urllib.request

url = "http://www.baidu.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}
# 创建请求对象
request = urllib.request.Request(url,headers=headers)
# 获取响应对象
response = urllib.request.urlopen(request)
# 获取内容
html = response.read().decode()

print(html)
print(response.getcode()) # 返回HTTP响应码
print(response.geturl())  # 返回实际数据的URL地址