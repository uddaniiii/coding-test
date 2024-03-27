def solution(keyinput, board):
    answer = [0,0]
    for k in keyinput:
        if k=="left":
            answer[0]-=1
        elif k=="right":
            answer[0]+=1
        elif k=='up':
            answer[1]+=1
        elif k=='down':
            answer[1]-=1
        
        for i in range(len(answer)):
            if abs(answer[i])>board[i]//2:
                answer[i]= (board[i]//2 if answer[i]>0 else -(board[i]//2))
                
    return answer