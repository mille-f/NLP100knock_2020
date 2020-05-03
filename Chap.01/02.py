str1 = "パトカー"
str2 = "タクシー"
ans = ""

for (s1, s2) in zip(str1, str2):
    ans += s1 + s2

print(ans)