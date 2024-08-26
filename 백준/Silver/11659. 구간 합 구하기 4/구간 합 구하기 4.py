import sys
input = sys.stdin.readline

n, q=map(int,input().split())
nList=list(map(int,input().split()))

sumRes=0
prefix_sum=[0]
for i in nList:
    sumRes+=i
    prefix_sum.append(sumRes)

res=[]
for i in range(q):
    s,e=map(int,input().split())
    res.append(prefix_sum[e]-prefix_sum[s-1])
    print(prefix_sum[e]-prefix_sum[s-1])