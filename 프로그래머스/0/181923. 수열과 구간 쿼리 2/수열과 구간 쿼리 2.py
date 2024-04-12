def solution(arr, queries):
    res=[]
    for s,e,k in queries:
        num=-1
        numList=sorted(arr[s:e+1])
        for n in numList:
            if n>k:
                num=n
                break
        res.append(num)
    return res