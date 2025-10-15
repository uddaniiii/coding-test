n=int(input())

i=2
iArray=[]
while n!=1:
    if n%i==0:
        iArray.append(i)
        n//=i
    else:
        i+=1
print(*sorted(iArray),sep='\n')