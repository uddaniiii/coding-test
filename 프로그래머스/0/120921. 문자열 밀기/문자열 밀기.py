def solution(A, B):
    i=0
    cnt=0
    while i<len(A):
        if A==B:
            return cnt
        A=A[-1]+A[:len(A)-1]
        cnt+=1
        i+=1
    return -1