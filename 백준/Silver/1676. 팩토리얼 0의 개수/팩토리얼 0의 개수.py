import math

n=int(input())

res=math.factorial(n)
res=list(str(res))[-1:0:-1]

cnt=0
for c in res:
    if c=='0':
        cnt+=1
    if c!='0':
        break
print(cnt)