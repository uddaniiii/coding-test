N=int(input())

arr=[]
for i in range(N):
    x,y=map(int,input().split())
    arr.append([x,y])
# print(arr)

arr = sorted(arr,key=lambda x:(x[0],x[1]))
for x,y in arr:
    print(x,y)