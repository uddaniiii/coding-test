n=int(input())

nList=[]
cmd=[]
for _ in range(n):
    cmd.append(input())

for c in cmd:
    if c.startswith("push"):
        _, x=c.split()
        nList.append(x)
    elif c=="pop":
        if not nList:
            print(-1)
        else:
            print(nList.pop(0))
    elif c=="size":
        print(len(nList))
    elif c=="empty":
        print(0 if nList else 1)
    elif c=="front":
        if not nList:
            print(-1)
        else:
            print(nList[0])
    elif c=="back":
        if not nList:
            print(-1)
        else:
            print(nList[-1])        
