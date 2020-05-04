with open('popular-names.txt') as f:
    cols = sorted(f, key=lambda n: int(n.split('\t')[2]), reverse=True)

print(''.join(cols))

# UNIXコマンド
# sort -rk3 popular-names.txt