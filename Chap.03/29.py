import re
import requests

dic = {}
reg = re.compile(r'\|(.+?)\s=\s*(.+)')

with open('uk.txt') as f:
    for line in f:
        r = re.findall(reg, line)
        if r:
            dic[r[0][0].rstrip()] = r[0][1]

url = 'https://commons.wikimedia.org/w/api.php'
params = {"action": "query", "format": "json", "titles": "File:" + dic['国旗画像'], "prop": "imageinfo", "iiprop": "url"}
req = requests.Session().get(url=url, params=params)
res = req.json()
pages = res['query']['pages']

for key, val in pages.items():
    print(val['imageinfo'][0]['url'])