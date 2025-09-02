word=input().upper()

cnt={}
for w in word:
    if w in cnt:
        cnt[w]+=1
    else:
        cnt[w]=1

max_val=max(cnt.values())
max_keys=[k for k,v in cnt.items() if v==max_val]
if len(max_keys)>1:
    print("?")
else:
    print(max_keys[0])