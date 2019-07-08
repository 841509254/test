import re

s = "A B C D"

p = re.compile("(\w+)\s+\w+\s+(\w+)")
r1 = p.findall(s)

print(r1)