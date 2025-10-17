n=int(input())
nArr=set(map(int, input().split()))

m=int(input())
mArr=list(map(int, input().split()))

res=[]
for i in mArr:
    if i in nArr:
        res.append(1)
    else:
        res.append(0)

print(*res)