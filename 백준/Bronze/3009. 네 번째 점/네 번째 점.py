xArr=[]
yArr=[]
for _ in range(3):
    x,y=map(int,input().split())
    xArr.append(x)
    yArr.append(y)
# print(xArr)

xCnt={}
for x in xArr:
    xCnt[x]=xArr.count(x)
# print(xCnt)

yCnt={}
for y in yArr:
    yCnt[y]=yArr.count(y)

print(min(xCnt,key=xCnt.get), min(yCnt,key=yCnt.get))