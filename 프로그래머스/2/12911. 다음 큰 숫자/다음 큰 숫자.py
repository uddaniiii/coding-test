def solution(n):
    i=n+1
    while str(bin(n)[2:]).count('1') != str(bin(i)[2:]).count('1'):
        i+=1
    return i
