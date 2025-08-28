num=[]
for _ in range(9):
    num.append(list(map(int,input().split())))

maxNum=max(map(max,num))
print(maxNum)
for i in range(9):
    if maxNum in num[i]:
        print(i+1, num[i].index(maxNum)+1,end=' ')