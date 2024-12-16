t=int(input())

nList=[]
for i in range(t):
    nList.append(list(map(int,input().split())))

for a,b in nList:
    print(a+b)