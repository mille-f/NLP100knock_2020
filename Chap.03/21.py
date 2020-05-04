l = []

with open('uk.txt') as f:
    for line in f:
        if '[[Category:' in line:
            l.append(line.rstrip().split('\n'))

print('\n'.join(sum(l, [])))