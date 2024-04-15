def solution(a, b):
    x,y=a,b
    while y!=0:
        x,y=y,x%y
    b=b/x
    factors=[]
    for i in range(2,int(b**0.5)+1):
        while b%i==0:
            factors.append(i)
            b//=i
    if b > 1:
        factors.append(b)
        
    if any(factor not in [2, 5] for factor in factors):
        return 2
    else:
        return 1
