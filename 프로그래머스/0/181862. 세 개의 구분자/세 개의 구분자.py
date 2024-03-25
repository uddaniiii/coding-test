def solution(myStr):
    for s in myStr:
        if s=='a' or s=='b' or s=='c':
            myStr=myStr.replace(s,' ')
    return myStr.split() if myStr.split() else ["EMPTY"]