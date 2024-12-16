n=int(input())

for _ in range(n):
    res=''
    r,s=input().split()
    for i in s:
        res+=''.join(int(r)*i)
    print(res)  