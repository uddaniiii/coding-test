a,b,c=map(int, input().split())

sticks=sorted([a,b,c])

if sticks[2]<sticks[0]+sticks[1]:
    print(sum(sticks))
else:
    sticks[2]=sticks[0]+sticks[1]-1
    print(sum(sticks))