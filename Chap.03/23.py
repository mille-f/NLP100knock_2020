l = []

with open('uk.txt') as f:
    for line in f:
        if '==' in line:
            l.extend(line.rstrip().split('\n'))

for line in l:
    n = line.count('=')//2 -1
    line = line.lstrip('= ').rstrip(' =')
    print(f'{line} {n}')