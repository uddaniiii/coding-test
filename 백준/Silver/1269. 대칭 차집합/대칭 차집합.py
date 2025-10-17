a,b=map(int,input().split())
setA=set(list(input().split()))
setB=set(list(input().split()))

print(len((setA-setB)|(setB-setA)))
