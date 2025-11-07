n=int(input())
nList=list(map(int,input().split()))

stack=[]
i=1
for num in nList:
    stack.append(num)
    while stack and stack[-1]==i:
        stack.pop()
        i+=1
print("Nice" if not stack else "Sad")