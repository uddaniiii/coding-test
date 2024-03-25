def solution(i, j, k):
    l=''.join(str(n) for n in range(i,j+1))
    return l.count(str(k))