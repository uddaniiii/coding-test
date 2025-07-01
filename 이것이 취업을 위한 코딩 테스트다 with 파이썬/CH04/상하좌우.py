N=int(input())
A=input().split()

dir={'L':[0,-1],'R':[0,1],'U':[-1,0],'D':[1,0]}

x,y=1,1
for i in A:
    dy,dx=dir[i]
    # print(f"dx={dx}, dy={dy}")
    if x+dx>=1 and x+dx<=N and y+dy>=1 and y+dy<=N:
        x,y=x+dx,y+dy
print(y,x)