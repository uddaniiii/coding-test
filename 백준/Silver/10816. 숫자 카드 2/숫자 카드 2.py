from collections import Counter

n=int(input())
nList=list(map(int, input().split()))
m=int(input())
mList=list(map(int, input().split()))

count=Counter(nList)
res=[count[i] for i in mList]
print(*res)