N=int(input())

info=[]
for i in range(N):
    info.append( input().split())
# print(info)

print(*[name for name,score in sorted(info, key=lambda x: x[1])])
