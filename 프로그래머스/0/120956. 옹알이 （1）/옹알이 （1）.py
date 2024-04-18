def solution(babbling):
    word=["aya", "ye", "woo", "ma"]
    cnt=0
    for i in range(len(babbling)):
        for w in word:
            if w in babbling[i]:
                babbling[i]=babbling[i].replace(w,' ')
        if not babbling[i].strip():
            cnt+=1
    return cnt