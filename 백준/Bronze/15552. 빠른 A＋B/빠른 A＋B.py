import sys

t=sys.stdin.readline
t = int(t().strip())

for i in range(t):
    a,b=map(int, sys.stdin.readline().strip().split())
    print(a+b)
