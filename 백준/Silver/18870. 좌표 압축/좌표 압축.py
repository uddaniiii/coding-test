n=int(input())
nList=list(map(int, input().split()))

setList=sorted(set(nList))

coord={}
for i,num in enumerate(setList):
    coord[num]=i

print(*list(coord[j] for j in nList))