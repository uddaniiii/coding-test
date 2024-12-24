import math

n=int(input())
wList=[]
for _ in range(n):
    wList.append(input())
print(*sorted(set(wList), key=lambda x:(len(x), x)),sep='\n')
