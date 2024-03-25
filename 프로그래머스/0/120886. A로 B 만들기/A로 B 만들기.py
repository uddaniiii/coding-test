def solution(before, after):
    before=list(before)
    for a in after:
        if a in before:
            before.remove(a)
        else:
            return 0
    return 1