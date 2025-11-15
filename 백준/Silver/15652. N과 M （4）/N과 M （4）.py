n,m=map(int,input().split())

path=[]

def backtrack(): 
    if len(path)==m:
        print(*path)
        return

    for i in range(1,n+1):
            if path:
                if path[-1]<=i:
                    path.append(i)
                else:
                    continue
            else:
                 path.append(i)   
            backtrack()
            path.pop()
backtrack()