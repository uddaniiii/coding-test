def solution(s, n):
    res=''
    for c in s:
        if c>='A' and c<='Z':
            res+=chr((ord(c)-ord('A')+n)%26+ord('A'))
        elif c>='a' and c<='z':
            res+=chr((ord(c)-ord('a')+n)%26+ord('a'))
        else:
            res+=c
    return res