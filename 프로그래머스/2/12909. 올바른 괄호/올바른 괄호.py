def solution(s):
    res=[]
    for i,c in enumerate(s):
        if i==0 and c==')':
            return False 
        else:
            if c==')':
                if res and res[-1]=='(':
                    res.pop()
            elif c=='(':
                res.append(c)
    
    return False if res else True