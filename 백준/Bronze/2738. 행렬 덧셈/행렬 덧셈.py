n,m=map(int,input().split())
a,b=[],[]
for _ in range(n):
    a.append(list(map(int,input().split())))
for _ in range(n):
    b.append(list(map(int,input().split())))

res=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        res[i][j]=a[i][j]+b[i][j]

for r in res:
    print(*r)