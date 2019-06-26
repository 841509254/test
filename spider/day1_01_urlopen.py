#! coding=utf-8
import urllib.request

url = "http://www.baidu.com/"
# 向网站发起请求并获取响应对象
response = urllib.request.urlopen(url)

html = response.read().decode("utf-8")
print(html)

# 此方法不支持重构User-Agent