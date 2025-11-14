a1,a0=map(int,input().split())
c=int(input())
n0=int(input())

# a1 < c 인 경우
if a1 < c:
    if a1*n0 + a0 <= c*n0:
        print(1)
    else:
        print(0)

# a1 == c 인 경우
elif a1 == c:
    if a0 <= 0:
        print(1)
    else:
        print(0)

# a1 > c 인 경우
else:
    print(0)