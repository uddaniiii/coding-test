n=int(input())
score=0
for _ in range(n):
    s=input()
    score=0
    o=0
    for c in s:
        if c=='O':
            o+=1
            score+=o
        else:
            o=0
    print(score)
