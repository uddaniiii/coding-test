import math

m,n = map(int, input().split())

for i in range(m,n+1):
    is_prime=True
    if i<2:
        is_prime=False
    else:
        for j in range(2, int(i**0.5)+1):
            if i%j==0:
                is_prime=False
                break
    
    if is_prime:
        print(i)