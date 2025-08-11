n,m=map(int, input().split())

array=[0]*n
# print(array)

for _ in range(m):
    i,j,k=map(int, input().split())

    for i in range(i-1,j):
        array[i]=k
print(*array)