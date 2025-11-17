n=int(input())
nList=list(map(int,input().split()))

res=0
nList.sort()
# print(nList)
for i in range(1,len(nList)+1):   
    # print(nList[:i]) 
    res+=sum(nList[:i])

print(res)