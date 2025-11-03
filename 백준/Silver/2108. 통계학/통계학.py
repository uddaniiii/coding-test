from collections import Counter
import sys

input = sys.stdin.readline
n=int(input())

nList = [int(input()) for _ in range(n)]

avg = sum(nList)/n
if avg >= 0:
    print(int(avg + 0.5))
else:
    print(int(avg - 0.5))

# print(nList)
nList.sort()

print(nList[len(nList)//2])

nDict=Counter(nList)
# print(nDict)
maxRes=max(nDict.values())
maxKey=[k for k,v in nDict.items() if v==maxRes]
maxKey.sort()
# print(maxKey)
print(maxKey[1] if len(maxKey)>1 else maxKey[0])


print(nList[-1]-nList[0])