def solution(array, n):
    array=sorted(array)
    res=[]
    for i in array:
        res.append(abs(i-n))
        
    return array[res.index(min(res))]
