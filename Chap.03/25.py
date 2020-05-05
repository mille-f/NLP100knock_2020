import re

dic = {}
reg = re.compile(r'\|(.+?)\s=\s*(.+)')

with open('uk.txt') as f:
    for line in f:
        r = re.findall(reg, line)
        if r:
            dic[r[0][0].rstrip()] = r[0][1]

print(dic)