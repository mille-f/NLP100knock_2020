with open('popular-names.txt') as f:
    c1 = [line.split('\t')[0] for line in f]

print('\n'.join(sorted(set(c1))))

# UNIXコマンド
# cut -f1 poplar-names.txt | sort | uniq