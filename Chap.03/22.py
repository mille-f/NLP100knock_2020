l = []

with open('uk.txt') as f:
    for line in f:
        if '[[Category:' in line:
            l.extend(line.rstrip().split('\n'))

for line in l:
    print(line.replace('[[Category:', '').replace('|*', '').replace(']]', ''))