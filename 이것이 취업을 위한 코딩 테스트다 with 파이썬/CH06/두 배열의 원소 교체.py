# 1번 방법

'''
N,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

for i in range(K):
    a=A.index(min(A))
    b=B.index(max(B))
    A[a],B[b]=B[b],A[a]

print(sum(A))
'''

# 2번 방법

N,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i]<B[i]:
        A[i],B[i]=B[i],A[i]
    else:
        break

print(sum(A))
