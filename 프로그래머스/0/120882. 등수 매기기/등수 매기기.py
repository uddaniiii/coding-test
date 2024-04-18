def solution(scores):
    avg_scores = [(sum(score) / 2, i + 1) for i, score in enumerate(scores)]
    avg_scores.sort(key=lambda x: (-x[0], x[1]))
    
    ranks = [0] * len(scores)
    rank = 1
    prev_score = avg_scores[0][0]
    for i, (score, student_num) in enumerate(avg_scores):
        if score != prev_score:
            rank = i + 1
        ranks[student_num - 1] = rank
        prev_score = score

    return ranks