def solution(myStr):

    if 'a' in myStr or 'b' in myStr or 'c' in myStr:
        myStr=myStr.replace('a',' ')
        myStr=myStr.replace('b',' ')
        myStr=myStr.replace('c',' ')
    return myStr.split() if myStr.split() else ["EMPTY"]