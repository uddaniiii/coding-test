from collections import deque

n=int(input())
nList=deque(range(1,n+1))

while len(nList)>1:
    nList.popleft()
    nList.append(nList.popleft())
print(*nList)