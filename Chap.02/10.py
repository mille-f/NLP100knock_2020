cnt = 0
with open('popular-names.txt') as f:
    for line in f:
        #print(line, end='')
        cnt+=1

print(cnt)

# UNIXコマンド
# wc -l popular-names.txt