k=int(input())

nList=[]
for _ in range(k):
    i = int(input())

    if i==0:
        nList.pop(-1)
    else:
        nList.append(i)

print(sum(nList))