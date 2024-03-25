def solution(emergency):
    d={}
    e1 = emergency
    for i,n in enumerate(sorted(e1,reverse=True)):
        d[n]=i+1

    return [d[i] for i in emergency if i in d.keys()]