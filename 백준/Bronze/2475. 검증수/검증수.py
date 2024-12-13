n=input().split()

print(sum(int(i)**2 for i in n)%10)