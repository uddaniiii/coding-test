# import sys
# input=sys.stdin.readline
t=int(input())

for _ in range(t):
    vps=input()

    stack=[]
    for i in vps:
        if i=='(':
            stack.append(i)
        elif i==')':
            if stack:
                stack.pop(-1)
            else:
                print("NO")   
                break
    else:
        if stack:
            print("NO")
        else:
            print("YES")