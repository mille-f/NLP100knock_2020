
import MeCab

res = []
map = {}

with open('neko.txt.mecab') as f:
    txt = f.read().split('\n')

for line in txt:
    if line != 'EOS':
        l = line.split('\t')
        if  l[0] != '' :
            rear = l[1].split(',')
        map = {'surface':l[0], 'base':rear[6], 'pos':rear[0], 'pos1':rear[1]}
        res.append(map)

noun = []
tmp = ''
for map in res:
    if map['pos'] == '名詞':
        tmp += map['surface']
    else:
        if tmp != '':
            noun.append(tmp)
            tmp = ''

print(noun)