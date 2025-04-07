N,M=map(int, input().split())
length=list(map(int, input().split()))

start=0
end=max(length)

while start<=end:
    mid=(start+end)//2
    total=0
    for i in length:
        if i>mid:
            total+=i-mid
    if total>=M:
        result=mid
        start=mid+1
    else:
        end=mid-1

print(result)