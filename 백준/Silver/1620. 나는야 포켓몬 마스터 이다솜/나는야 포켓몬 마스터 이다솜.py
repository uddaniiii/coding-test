n,m=map(int,input().split())

book={}
for i in range(1,n+1):
    name=input()
    book[i]=name
    book[name]=i

for _ in range(m):
    info=input()
    if info.isalpha():
        print(book[info])
    else:
        print(book[int(info)])