def ngram(seq, n):
    #for i in range(len(seq)-n+1):
    #    print(str(i) + ':' + str(i+n) + '=' + seq[i:i+n])
    return [seq[i:i+n] for i in range(len(seq)-n+1)]

# 単語bi-gram
s = "I am an NLPer"
print(ngram(s, 2))

# 文字bi-gram
w = s.split(" ")
print(ngram(w, 2))