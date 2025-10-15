import sys
for line in sys.stdin:
    a,b,c=map(int,line.split())
    # print(a,b,c)
    if a==b==c==0:
        break
    if max(a,b,c)>=(a+b+c)-max(a,b,c):
        print("Invalid")
    elif a==b==c:
        print("Equilateral") 
    elif a==b or b==c or a==c:
        print("Isosceles")
    elif a!=b and b!=c and c!=a:
        print("Scalene")
    elif a+b+c!=180:
        print("Error")
    