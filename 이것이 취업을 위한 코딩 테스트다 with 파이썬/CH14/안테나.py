N=int(input())
house=list(map(int, input().split()))
# print(house)

house.sort()
print(house[(len(house)-1)//2])