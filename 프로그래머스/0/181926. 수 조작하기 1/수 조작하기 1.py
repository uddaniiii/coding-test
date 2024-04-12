def solution(n, control):
    wasd={'w':1,'s':-1,'d':10,'a':-10}
    for c in control:
        if c in wasd:
            n+=wasd[c]
    return n