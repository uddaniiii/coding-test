MAX = 1000000
prime=[True]*(MAX+1)
prime[0]=prime[1]=False

for i in range(2,int(MAX**0.5)+1):
    if prime[i]:
        for j in range(i*i,MAX+1,i):
            prime[j]=False

t=int(input())
for _ in range(t):
    n=int(input())
    count = 0
    for a in range(2, n//2 + 1):  
        if prime[a] and prime[n - a]: # 소수의 합 확인
            count += 1
    print(count)