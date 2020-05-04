with open('popular-names.txt') as f0,\
    open('col1.txt', 'w') as f1,\
    open('col2.txt', 'w') as f2:
    for line in f0:
        cols = line.rstrip('\n').split('\t')
        print(cols[0], file=f1)
        print(cols[1], file=f2)

# UNIXコマンド
# cut -f 1  popular-names.txt > col1.txt
# cut -f 2  popular-names.txt > col2.txt