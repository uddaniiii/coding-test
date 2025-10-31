n=int(input())

res=0
nameList=[]
for _ in range(n):
    chat=input()

    if chat=='ENTER':
        res+=len(set(nameList))
        nameList=[]
        continue
    else:
        nameList.append(chat)

res+=len(set(nameList))
print(res)