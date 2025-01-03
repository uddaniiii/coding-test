import sys
n=int(sys.stdin.readline())

def roundUp(x):
    return int(x) + (1 if x - int(x) >= 0.5 else 0)

nList=[]
if n==0:
    print(0)
else:   
    for _ in range(n):
        nList.append(int(sys.stdin.readline()))

    trim=roundUp(n*0.15)
    nList=sorted(nList)[trim:n-trim]
    print(roundUp(sum(nList)/len(nList)))