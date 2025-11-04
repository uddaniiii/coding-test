n,k=map(int,input().split())
tList=list(map(int,input().split()))

current_sum=sum(tList[:k])
max_sum=current_sum
for i in range(k,n):
    current_sum=current_sum-tList[i-k]+tList[i]
    if max_sum<current_sum:
        max_sum=current_sum
print(max_sum)