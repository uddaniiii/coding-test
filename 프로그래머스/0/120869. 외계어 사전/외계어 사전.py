def solution(spell, dic):
    res=0
    for d in dic:
        if sorted(list(d))==sorted(spell):
            res+=1
    return 1 if res>0 else 2