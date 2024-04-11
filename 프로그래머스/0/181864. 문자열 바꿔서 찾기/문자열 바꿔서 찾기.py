def solution(myString, pat):
    res=''
    for s in myString:
        if s=='A':
            res+='B'
        elif s=='B':
            res+='A'
    return int(pat in res)