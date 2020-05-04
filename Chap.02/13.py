with open('col1.txt') as f1, open('col2.txt') as f2:
    for col1, col2 in zip(f1, f2):
        col1 = col1.rstrip()
        col2 = col2.rstrip()
        print(f'{col1}\t{col2}')

# UNIXコマンド
# paste col1.txt col2.txt