n = int(input())
l, d = [], []
cnt = 1

with open('popular-names.txt') as f:
    for line in f:
        l.append(line)

r = len(l)
p = r//n if r%n == 0 else r//n + 1

for i in range(0, r, p):
    d.append(l[i:i+p])

for i, s in enumerate(d, 1):
    with open(f'popular-names_{i}.txt', 'w') as f:
        f.write(''.join(s))

# UNIXコマンド
# split -l 5 popular-names.txt