def solution(arr):
    i=0
    while 2**i<len(arr):
        i+=1
    
    for i in range((2**i)-len(arr)):
        arr.append(0)
    return arr