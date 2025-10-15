m=int(input())
n=int(input())

nArray=[]
for i in range(m,n+1):
    if i>1:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else: # for문이 break 없이 끝까지 돌았을때 실행
            nArray.append(i) 
# print(nArray)

print(sum(nArray), min(nArray),sep='\n') if nArray else print(-1)