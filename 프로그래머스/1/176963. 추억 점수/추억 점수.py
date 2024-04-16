def solution(name, yearning, photo):
    score_dict= dict(zip(name,yearning))
    answer = []
    for p in photo:
        score=0         
        for n in p:
            if n in score_dict.keys():
                score+=score_dict[n]
        answer.append(score)
    return answer