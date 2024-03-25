def solution(arr):
    x1=arr
    x2=[]
    i=0
    while True:
        x2=[]
        for a in x1:
            if a>=50 and a%2==0:
                x2.append(a/2)
            elif a<50 and a%2:
                x2.append(a*2+1)
            else:
                x2.append(a)
        if x1==x2:
            return i 
        else:
            x1=x2 
        i+=1