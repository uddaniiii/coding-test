def solution(s):
    res=''
    word=[]
    for c in s.split(" "):
        word.append(c.strip())
    for w in word:
        for i,ch in enumerate(w):
            if i%2:
                res+=ch.lower()
            else:
                res+=ch.upper()
        res+=' '
    return res[:-1]