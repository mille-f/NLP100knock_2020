import re

dic = {}
reg1 = re.compile(r'\|(.+?)\s=\s*(.+)')
reg2 = re.compile(r'\'{2,}(.+?)\'{2,}')
reg3 = re.compile(r'\[\[(.+?)\]\]')
reg4 = re.compile(r'<br />|<ref.+?>|</ref>')

with open('uk.txt') as f:
    for line in f:
        line = re.sub(reg2, '\\1', line) # 強調マークアップ除去
        line = re.sub(reg3, '\\1', line) # 内部リンク除去
        line = re.sub(reg4, '', line) # MediaWikiマークアップ除去
        r = re.findall(reg1, line)
        if r:
            # タプル -> リスト
            e1, e2 = r[0]
            l = [e1, e2]
            dic[l[0]] = l[1]

print(dic)