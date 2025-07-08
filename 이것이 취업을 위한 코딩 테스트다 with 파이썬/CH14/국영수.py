N=int(input())

score=[input().split() for _ in range(N)]
# print(score)

score.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for s in score:
    print(s[0])s