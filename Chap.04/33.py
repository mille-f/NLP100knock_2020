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
for i in range(len(res)):
    if res[i]['pos'] == '名詞' and res[i+1]['surface'] == 'の' and res[i+2]['pos'] == '名詞':
        noun.append(res[i]['surface'] + res[i+1]['surface'] + res[i+2]['surface'])

print(noun)