with open('popular-names.txt') as f:
    for line in f:
        print(line.replace('\t', ' '), end='')

# UNIXコマンド
# sed -e 's/\t/ /g' popular-names.txt | less