l=int(input())

numList=list(input())

res=0
for i, n in enumerate(numList):
    n=ord(n)-96
    res+=n*31**i
print(res)