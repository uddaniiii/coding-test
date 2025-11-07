from collections import deque
n,k=map(int,input().split())

queue=deque(i+1 for i in range(n))
res=[]
while queue:
    queue.rotate(-(k-1))
    # print(queue)
    res.append(queue.popleft())

print("<",end='')
print(*res,sep=', ',end='')
print(">")