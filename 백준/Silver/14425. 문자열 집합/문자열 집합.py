n,m=map(int,input().split())
s=[]
for _ in range(n):
    s.append(input())

cnt=0
for i in range(m):
    if input() in s:
        cnt+=1
print(cnt)