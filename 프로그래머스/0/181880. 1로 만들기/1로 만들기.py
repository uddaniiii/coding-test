def solution(num_list):
    i=0
    for n in num_list:
        while n!=1:
            if n%2:
                n=(n-1)/2
            else:
                n=n/2
            i+=1
        
    return i