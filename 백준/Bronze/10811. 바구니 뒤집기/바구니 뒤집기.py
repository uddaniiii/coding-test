n,m=map(int, input().split())

array=[0]*n
for i in range(n):
    array[i]=i+1

for _ in range(m):
    i,j=map(int, input().split())
    array[i-1:j] = reversed(array[i-1:j])
print(*array)