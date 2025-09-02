n=int(input())

words=[]
for _ in range(n):
    words.append(input())

res=0
for word in words:
    group=[]
    wRes=True
    for i,w in enumerate(word):
        if i==0:
            group.append(w)
        else:
            if word[i-1]!=w and w not in group:
                group.append(w)
            elif word[i-1]!=w and w in group:
                wRes=False
        # print(group, w, wRes)
    if wRes:
        res+=1
print(res)