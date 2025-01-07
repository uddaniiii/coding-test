n=int(input())

sList=list(map(int,input().split()))
t,p=map(int,input().split())

tshirt=[s//t if s%t==0 else s//t+1 for s in sList]
print(sum(tshirt))
print(n//p, n%p)