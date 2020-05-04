
import random

def typoglycemia(S):
    l = []
    for s in S:
        if len(s) > 4:
            #r = list(s[1:-1])
            #random.shuffle(r)
            #r = ''.join(r)
            r = ''.join(random.sample(list(s[1:-1]), len(s)-2))
            s = s[0]+r+s[-1]
        l.append(s)
    return ' '.join(l)

s = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(typoglycemia(s.split(" ")))