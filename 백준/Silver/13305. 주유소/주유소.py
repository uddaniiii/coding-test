n=int(input())
distance=list(map(int,input().split()))
cost=list(map(int,input().split()))

minCost=cost[0]
total=0

for i in range(n-1):
    if cost[i] < minCost:
        minCost = cost[i]
    total += minCost * distance[i]

print(total)