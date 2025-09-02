t=int(input())
cList=[int(input()) for _ in range(t)]
# print(cList)

q,d,n,p=0,0,0,0
for c in cList:
    q=c//25
    c%=25
    # print(c)
    d=c//10
    c%=10
    n=c//5
    c%=5
    p=c//1
    c%=1
    print(q,d,n,p)