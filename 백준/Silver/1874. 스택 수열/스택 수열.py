n=int(input())

nList=[]
for _ in range(n):
    nList.append(int(input()))

j=1
stack=[]
result=[]
for i in nList:
    while j<=i:
        stack.append(j)
        result.append('+')
        j+=1

    if stack[-1]==i:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        exit(0)

print(*result,sep='\n')
