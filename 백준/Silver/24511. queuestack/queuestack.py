from collections import deque

n=int(input())
nA=list(map(int,input().split()))
nB=list(map(int,input().split()))
m=int(input())
c=list(map(int,input().split()))

nList=deque()
for i in range(len(nA)):
    if nA[i]==0:
        nList.append(nB[i])

for j in c:
    nList.appendleft(j)
    print(nList.pop(),end=' ')