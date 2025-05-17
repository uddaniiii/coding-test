N=int(input())

num=[]
for i in range(N):
    num.append(int(input()))

print(*sorted(num,reverse=True),sep=" ")