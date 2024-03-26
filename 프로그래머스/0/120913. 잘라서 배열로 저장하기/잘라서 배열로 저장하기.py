def solution(my_str, n):
    l= len(my_str)//n if len(my_str)/n == int(len(my_str)/n) else len(my_str)//n+1
        
    return [my_str[i*n:i*n+n] for i in range(l)]