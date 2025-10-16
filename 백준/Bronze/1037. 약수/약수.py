n=int(input())
nArr=list(map(int, input().split()))
print(sorted(nArr)[0]*sorted(nArr)[-1])