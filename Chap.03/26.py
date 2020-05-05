import re

dic = {}
reg1 = re.compile(r'\|(.+?)\s=\s*(.+)')
reg2 = re.compile(r'\'{2,}(.+?)\'{2,}')

with open('uk.txt') as f:
    for line in f:
        r = re.findall(reg1, line)
        if r:
            # タプル -> リスト
            e1, e2 = r[0]
            l = [e1, e2]
            for match in re.finditer(reg2, line):
                #print(match.group(0)) # 強調除去前
                #print(match.group(1)) # 強調除去後
                m = [match.group(0), match.group(1)]
                r = re.sub(m[0], m[1], line).strip('|,\n').split(' = ')
                l = [r[0], r[1]]
            dic[l[0]] = l[1]

print(dic)