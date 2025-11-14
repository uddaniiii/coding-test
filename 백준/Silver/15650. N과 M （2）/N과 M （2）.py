n,m=map(int,input().split())

path=[]

def backtrack(start=1): 
    if len(path)==m:
        print(*path)
        return

    for i in range(start,n+1):
            path.append(i)
            backtrack(i+1)
            path.pop()
backtrack()