n=int(input())

sArr=set()
for _ in range(n):
    name, status=input().split()
    if status=="enter":
        sArr.add(name)
    else:
        sArr.remove(name)
    
print(*sorted(sArr,reverse=True),sep='\n')