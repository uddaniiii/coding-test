t=int(input())
dp=[None]*101
dp[1] = dp[2] = dp[3] = 1
# print(dp)
for i in range(4,101):
    dp[i] = dp[i-2] + dp[i-3]

for _ in range(t):
    print(dp[int(input())])