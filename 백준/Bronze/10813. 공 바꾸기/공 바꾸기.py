n,m=map(int, input().split())

array=[0]*n
for i in range(n):
    array[i]=i+1

for _ in range(m):
    i,j=map(int, input().split())
    array[i-1],array[j-1]=array[j-1],array[i-1]
print(*array)