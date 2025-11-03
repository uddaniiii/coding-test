n,b=map(int,input().split())
if n==0:
    print(0)

digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

res=''
while n>0:
    res=digits[n%b]+res
    n//=b
print(res)