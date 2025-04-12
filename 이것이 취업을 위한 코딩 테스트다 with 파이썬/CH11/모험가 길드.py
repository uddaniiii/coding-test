N=int(input())
array=list(map(int, input().split()))
array.sort()
group=[]
res=0
for i in array:
    group.append(i) # 여기서 굳이 리스트를 쓸 필요 없이 count로 +1해도 됨
    if i<=len(group):
        res+=1
        group=[]
print(res)