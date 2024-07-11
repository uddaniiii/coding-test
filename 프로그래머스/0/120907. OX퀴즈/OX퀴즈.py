def solution(quiz):
    answer = []
    for q in quiz:
        real_r=''
        a,b=q.split('=')
        real_r=real_r.join(a+'= '+str(eval(a)))
        if q==real_r:
            answer.append('O')
        else: answer.append('X')
    return answer