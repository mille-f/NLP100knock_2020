s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
ans = [len(x.strip(',.')) for x in s.split()]

print(ans)