def solution(arr, n):
    for idx,a in enumerate(arr):
        if len(arr)%2:
            if idx%2==0:
                arr[idx]+=n
        else:
            if idx%2:
                arr[idx]+=n
    return arr