def solution(s):
    return "".join(str(min([int(c) for c in s.split()]))+' '+str(max([int(c) for c in s.split()])))