loc=input()

col=ord(loc[0])-ord('a')+1
row=int(loc[1])
# print(col,row)

dir=[[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
count=0
for i in dir:
    new_col=col+i[0]
    new_row=row+i[1]
    if new_col>=1 and new_col<=8 and new_row>=1 and new_row<=8:
        count+=1

print(count)