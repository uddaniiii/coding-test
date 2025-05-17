# 1st

N,M=map(int,input().split())
x,y,d=map(int,input().split())

grid = [list(map(int, input().split())) for _ in range(N)]
# print(map)

bool_map=[[bool(int(x)) for x in row] for row in grid]
# print(bool_map)

directions={0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}

bool_map[x][y]=True
cnt,res=0,1
nd=0
while True:
    # print(f"x, {x}, y: {y}, d: {d}")
    if d==0:
        nd=3
    else:
        nd=d-1

    # print(x, directions[nd][0])
    nx=x+directions[nd][0]
    ny=y+directions[nd][1]
    # print(f"nx: {nx}, ny: {ny}, d: {d}, nd: {nd}")
    d=nd

    if bool_map[nx][ny]==False:
        bool_map[nx][ny]=True
        res+=1
        # print(f"res: {res}")
        x,y=nx,ny
        cnt=0
    else:
        cnt+=1

    if cnt==4:
        nx=x+directions[(d+2)%4][0]
        ny=y+directions[(d+2)%4][1]
        if bool_map[nx][ny]==True:
            # print(bool_map)
            if grid[nx][ny]==1:
                break
            else:
                x,y=nx,ny
        cnt=0

print(res)

# 2nd

N,M=map(int,input().split())
x,y,d=map(int,input().split())

grid=[list(map(int,input().split())) for _ in range(N)]
# print(grid)

res=1
rotation=0
directions={0:[-1,0],1:[0,1],2:[1,0],3:[0,-1]}
while True:
    nd=d-1 if d>0 else d+3
    # print(nd)

    if grid[x+directions[nd][0]][y+directions[nd][1]]==0:
        x+=directions[nd][0]
        y+=directions[nd][1]
        d=nd
        rotation=0
        grid[x][y]=1
        res+=1
    else:
        rotation+=1
        d=nd
        if rotation==4:
            x-=directions[nd][0]
            y-=directions[nd][1]
            if grid[x][y]==1:
                break
            else:
                x+=directions[nd][0]
                y+=directions[nd][1]

print(res)