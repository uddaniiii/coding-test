n,k=map(int,input().split())
coinList=[int(input()) for _ in range(n)]

coinList.sort(reverse=True)

res=0
# print(coinList)
for c in coinList:
    if k>=c:
        res+=k//c
        k=k%c
print(res)