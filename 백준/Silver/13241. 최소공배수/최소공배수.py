def gcd(a,b):
    while b!=0:
        a,b=b,a%b   
    return a
a,b=map(int,input().split())
gcdRes=gcd(a,b)
res=int(gcdRes*(a/gcdRes)*(b/gcdRes))
print(res if res!=1 else a*b)
