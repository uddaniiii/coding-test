def solution(array):
    n_dic={}
    for a in list(set(array)):
        n_dic[a]=array.count(a)
    
    max_v=max(n_dic.values())
    max_keys = [k for k, v in n_dic.items() if v == max_v]
    
    if len(max_keys) == 1:
        return max_keys[0]
    else:
        return -1