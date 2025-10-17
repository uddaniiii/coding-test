n,m=map(int,input().split())

nArr=set()
mArr=set()
for _ in range(n):
    nArr.add(input())
for _ in range(m):
    mArr.add(input())

res=list(nArr&mArr)
print(len(res),*sorted(res),sep='\n',end='\n')
# print(list(nArr&mArr))