import sys
import math 

MAX=123456*2
is_prime=[True]*(MAX+1)
is_prime[0],is_prime[1]=False,False

for i in range(2,int(math.sqrt(MAX))+1):
    if is_prime[i]:
        for j in range(i*i,MAX+1,i):
            is_prime[j]=False

for line in sys.stdin:
    n=int(line)
    if n==0:
        break

    print(sum(is_prime[n+1:2*n+1]))


