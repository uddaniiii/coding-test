sList=[False]*30
for _ in range(28):
    sList[int(input())-1]=True

for s in range(len(sList)):
    if not sList[s]:
        print(s+1)
