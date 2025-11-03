n=int(input())

nameDict={'ChongChong':True}
for _ in range(n):
    a,b=input().split()
    if a=='ChongChong' or b=='ChongChong':
        nameDict[a]=True
        nameDict[b]=True
    elif a in nameDict.keys() and nameDict[a]==True:
        nameDict[a]=True
        nameDict[b]=True    
    elif b in nameDict.keys() and nameDict[b]==True:
        nameDict[a]=True
        nameDict[b]=True
    else:
        nameDict[a]=False
        nameDict[b]=False
print(list(nameDict.values()).count(True))