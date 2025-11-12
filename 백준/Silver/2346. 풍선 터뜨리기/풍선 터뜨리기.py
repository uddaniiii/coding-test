from collections import deque
n=int(input())
nList=list(map(int,input().split()))
queue=deque()
for i,num in enumerate(nList):
    queue.append((i+1,num))
# print(queue)

res=[]
while queue:
    idx,move=queue.popleft()
    res.append(idx)
    if move>0:
        queue.rotate(-(move-1))
    else:
        queue.rotate(-move)
print(*res,sep=' ')
