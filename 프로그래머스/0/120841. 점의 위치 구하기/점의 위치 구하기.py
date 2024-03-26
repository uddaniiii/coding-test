def solution(dot):
    if dot[0]>0:
        if dot[1]>0:
            res=1
        else:
            res=4
    else:
        if dot[1]<0:
            res=3
        else:
            res=2
        
    return res