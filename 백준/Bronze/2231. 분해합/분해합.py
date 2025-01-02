n=int(input())

start=max(1, n-len(str(n))*9)
result=0
for i in range(start,n):
    cal=i+sum(map(int,str(i)))
    if n==cal:
        result=i
        break

print(result)