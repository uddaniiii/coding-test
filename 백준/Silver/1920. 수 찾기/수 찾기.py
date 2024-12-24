n=int(input())
nList=set(map(int,input().split()))
m=int(input())
mList=list(map(int,input().split()))

res=[1 if m in nList else 0 for m in mList]

print(*res,sep='\n')