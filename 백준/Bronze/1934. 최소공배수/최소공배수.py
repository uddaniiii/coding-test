def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    gcdRes=gcd(a,b)
    print(gcdRes*(a//gcdRes)*(b//gcdRes))