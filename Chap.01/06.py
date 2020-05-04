def ngram(seq, n):
    return [seq[i:i+n] for i in range(len(seq)-n+1)]

s1 = "paraparaparadise"
s2 = "paragraph"
w = "se"
x = set(ngram(s1, 2))
y = set(ngram(s2, 2))

# 和集合
print(x|y)
# 積集合
print(x&y)
# 差集合
print(x-y)
# ’se’というbi-gramがXおよびYに含まれるか
print(w in x)
print(w in y)