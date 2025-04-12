def solution(s):
    answer = len(s)
    #print(s)
    for i in range(1,len(s)//2+1):
        res=''
        past=s[0:i]
        cnt=1
        #print(f"past={past}")
        for j in range(i,len(s),i):
            #print(f"s[j:j+i]:{s[j:j+i]}")
            if past==s[j:j+i]:
                cnt+=1
            else:
                res+=str(cnt)+past if cnt>=2 else past
                cnt=1
                past=s[j:j+i]
                #print(f"바뀐 past: {past}")
        res+=str(cnt)+past if cnt>=2 else past
        #print(f"res={res}")  
        answer=min(answer, len(res))
            
    return answer