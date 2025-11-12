n,m=map(int, input().split())
board=list(list(map(int,input().split())) for _ in range(n))
coord=list(list(map(int,input().split())) for _ in range(m))
# print(board, coord)

sumBoard=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        sumBoard[i][j]=board[i][j]
        if i>0:
            sumBoard[i][j]+=sumBoard[i-1][j]
        if j>0:
            sumBoard[i][j]+=sumBoard[i][j-1]
        if i>0 and j>0:
            sumBoard[i][j]-=sumBoard[i-1][j-1]

# print(sumBoard)
for x1,y1,x2,y2 in coord:
    x1,y1,x2,y2=x1-1,y1-1,x2-1,y2-1
    res=sumBoard[x2][y2]
    if x1>0:
        res-=sumBoard[x1-1][y2]
    if y1>0:
        res-=sumBoard[x2][y1-1]
    if x1>0 and y1>0:
        res+=sumBoard[x1-1][y1-1]
    print(res)