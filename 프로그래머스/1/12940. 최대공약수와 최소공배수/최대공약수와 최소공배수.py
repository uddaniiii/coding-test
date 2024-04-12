def solution(n, m):
    a,b=n,m
    while b!=0:
        a,b=b,a%b
    
    return a,(n*m)/a
