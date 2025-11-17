n=int(input())
nList=list(map(int,input().split()))

dp=[None]*n
dp[0]=nList[0]

for i in range(1,n):
    # print(i)
    dp[i]=max(nList[i],nList[i]+dp[i-1])
    # print(f"i={i}, dp[i]={dp[i]}")

print(max(dp))