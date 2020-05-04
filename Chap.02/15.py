from collections import deque

n = int(input())
l = []

with open('popular-names.txt') as f:
    # dequeの方がスマート
    # print(''.join(deque(f, n)))
    for line in f:
        l.append(line)

print(''.join(l[len(l)-n-1:len(l)]))

# UNIXコマンド
# tail -n 5 popular-names.txt