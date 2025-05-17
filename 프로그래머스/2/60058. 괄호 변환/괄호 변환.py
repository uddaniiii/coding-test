def split(w):
    open,close=0,0
    for i in w:
        # print(i)
        if '('==i:
            open+=1
        else:
            close+=1
        if open==close:
            return open+close
    return 0

def correct_u(u):
    array=[]
    if u[0]=='(':
        array.append('(')
    else:
        return False
    
    for i in range(1,len(u)):
        if '(' == u[i]:
            array.append('(')
        elif ')' == u[i] and array:
            array.pop()
    if not array:
        return True
    else: 
        return False
    
def solution(p):
    answer = ''
    if not p:
        return p
    
    index=split(p)
    # print(index)
    
    u=p[:index]
    v=p[index:]
    # print(u,v)
    
    correct=correct_u(u)
    # print(correct)
    
    empty=''
    if correct:
        answer = u + solution(v)
    else:
        empty = '('
        empty += solution(v)
        empty += ')'
        u_pop = u[1:-1]
        for ch in u_pop:
            if ch == '(':
                empty += ')'
            else:
                empty += '('
        answer = empty
    return answer