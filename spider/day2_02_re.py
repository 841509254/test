# -*- coding:utf-8 -*-

import re
html = """<div><p>Python虐我千百遍</p></div>
<div><p>我待Python如初恋</p></div>"""

# 贪婪匹配: .*
p = re.compile("<p>(.*)</p>",re.S)

r1 = p.findall(html)

print(r1)

# 非贪婪匹配: .*?
p = re.compile("<p>(.*?)</p>",re.S)

r2 = p.findall(html)

print(r2)

