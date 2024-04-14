def solution(s):
    stack=[]
    answer = -1
    for c in s:
        if stack and stack[-1]==c:
            stack.pop(-1)
        else:
            stack.append(c)
            
    return 0 if stack else 1