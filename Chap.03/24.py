import re

reg = re.compile(r'ファイル:(.+?)\|')

with open('uk.txt') as f:
    for line in f:
        r = re.findall(reg, line)
        if r:
            print(', '.join(r))