def gcd(x,y):
    while y:
        x,y=y,x%y
    return x

a,b=map(int,input().split())
c,d=map(int,input().split())

down=b*d
up=a*d+b*c

gRes=gcd(down,up)
print(up//gRes,down//gRes)