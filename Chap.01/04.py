s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
n = [1,5,6,7,8,9,15,16,19]
l = [x for x in s.split()]
ans = {}

for i, w in enumerate(l, 1):
    if i in n:
        ans[i] = w[0]
    else:
        ans[i] = w[0:2]

print(ans)