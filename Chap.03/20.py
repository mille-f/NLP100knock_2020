import json
import sys

for line in sys.stdin:
    dic = json.loads(line)
    if dic['title'] == 'イギリス':
        print(dic.get('text'))

# 抽出結果をuk.txtに書き出し
# gunzip -c jawiki-country.json.gz | python3 20.py > uk.txt