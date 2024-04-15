def solution(strings, n):
    s_dic=[]
    for s in strings:
        s_dic.append([s[n],s])
    return [i[1] for i in sorted(s_dic)]
