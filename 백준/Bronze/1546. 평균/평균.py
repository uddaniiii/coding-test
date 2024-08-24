n=int(input())
num=list(map(int,input().split()))
new_num=[]
for i in num:
    new_num.append(i/max(num)*100)
print(sum(new_num)/n)