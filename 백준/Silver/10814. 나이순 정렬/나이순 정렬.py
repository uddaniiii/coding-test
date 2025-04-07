N=int(input())

arr=[]
for i in range(N):
    age, name=input().split()
    arr.append([int(age), name, i])
# print(arr)

arr = sorted(arr,key=lambda x:(x[0],x[2]))
for age,name,_ in arr:
    print(age,name)