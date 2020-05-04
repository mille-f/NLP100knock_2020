NUM = 219

def cipher(S):
    l = []
    for c in S:
        if c.islower():
            c = chr(NUM-ord(c))
        l.append(c)
    return ''.join(l)

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
enc = cipher(s)
dec = cipher(enc)

print(enc)
print(dec)