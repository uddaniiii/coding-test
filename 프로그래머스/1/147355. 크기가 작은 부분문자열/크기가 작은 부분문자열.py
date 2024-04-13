def solution(t, p):
    part=[]
    answer=0
    for i in range(len(t)-len(p)+1):
        part.append(t[i:i+len(p)])
    
    for n in part:
        if n<=p:
            answer+=1
            
    return answer