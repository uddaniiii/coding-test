def solution(n, arr1, arr2):
    res1=[]
    for a in arr1:
        res1.append(bin(a)[2:].rjust(n,'0'))
    res2=[]
    for a in arr2:
        res2.append(bin(a)[2:].rjust(n,'0'))
    
    answer=[]
    for i in range(len(res1)):
        hash=''
        for j in range(len(res1[0])):
            if int(res1[i][j]) | int(res2[i][j]):
                hash+='#'
            else:
                hash+=' '
                
        answer.append(hash)
    return answer