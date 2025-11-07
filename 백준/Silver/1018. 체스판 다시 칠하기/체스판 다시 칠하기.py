n,m=map(int,input().split())

board=[]
for _ in range(n):
    board.append(input())

white=[[0]*m for _ in range(n)]
black=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if (i+j)%2==0:
            white[i][j]='W'
            black[i][j]='B'
        else:
            white[i][j]='B'
            black[i][j]='W'


choice=[]
# choice=board[0:8][0:8]
# print(choice)
res=[]
for i in range(n-7):
    # print(i)
    for j in range(m-7):
        # print(j)
        choice=[row[j:j+8] for row in board[i:i+8]]
        # print(choice)
        white_diff = 0
        black_diff = 0
        for x in range(8):
            for y in range(8):
                if choice[x][y] != white[x][y]:
                    white_diff += 1
                if choice[x][y] != black[x][y]:
                    black_diff += 1

        res.append(min(white_diff, black_diff))

print(min(res))