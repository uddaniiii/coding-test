def solution(my_string, n):
    res=""
    for i in my_string:
        res+=i.replace(i,i*n)
        
    return res