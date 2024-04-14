def solution(sizes):
    max_sizes=[]
    min_sizes=[]
    for s in sizes:
        max_sizes.append(max(s))
        min_sizes.append(min(s))
    return max(max_sizes)*max(min_sizes)
