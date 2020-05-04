from collections import Counter

with open('popular-names.txt') as f:
    c = Counter(line.split('\t')[0] for line in f)

for val, cnt in c.most_common():
    print(f'{cnt} {val}')

# UNIXコマンド
# cut -f1 popular-names.txt | sort | uniq -c | sort -r