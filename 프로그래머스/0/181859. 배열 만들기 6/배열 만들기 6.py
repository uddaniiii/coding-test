def solution(arr):
    stk = []
    i=0
    while i<len(arr):
        if not stk:
            stk.append(arr[i])
        elif stk and stk[-1]==arr[i]:
            stk.pop(-1)
        elif stk and stk[-1]!=arr[i]:
            stk.append(arr[i])
        i+=1

    return stk if stk else [-1]