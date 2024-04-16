def solution(k, score):
    answer = []
    s_list=[]
    for i in score:
        s_list.append(i)
        s_list=sorted(s_list,reverse=True)[:k] if len(s_list)>k else sorted(s_list,reverse=True)
        answer.append(s_list[-1])
    return answer