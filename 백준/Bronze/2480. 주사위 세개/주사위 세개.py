a,b,c=map(int, input().split())

if a==b==c:
    res=10000+a*1000
elif a==b or b==c or a==c:
    if a==b:
        res=1000+a*100
    elif b==c:
        res=1000+b*100
    else:
        res=1000+c*100
else:
    res=max(a,b,c)*100

print(res)