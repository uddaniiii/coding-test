n=int(input())
nArr=[]
for _ in range(n):
    nArr.append(int(input()))
print(*sorted(nArr),sep='\n')