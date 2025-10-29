import math

n=int(input())
for _ in range(n):
    num=int(input())

    if num<2:
        print(2)
        continue 
       
    resNum=0
    i=num
    while resNum==0:
        # print(f"i={i}")
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                break
        else:
            resNum=i
            break
        i+=1
    print(resNum)