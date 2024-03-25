def solution(strArr):
    d={}
    keys=[]
    for s in strArr:
        keys.append(len(s))
    d=dict.fromkeys(keys,0)
    
    for s in strArr:
        d[len(s)]+=1
        
    return max(d.values())
