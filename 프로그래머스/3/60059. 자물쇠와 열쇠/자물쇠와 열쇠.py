def rotation_matrix(matrix):
    return [list(row)[::-1] for row in zip(*matrix)]

def check(new_lock):
    lock_length=len(new_lock)//3
    for a in range(lock_length,lock_length*2):
        for b in range(lock_length,lock_length*2):
            if new_lock[a][b]!=1:
                return False
    return True

def solution(key, lock):
    new_lock=[[0]*len(lock)*3 for _ in range(len(lock)*3)]
    #print(new_lock)
    
    for i in range(len(lock),len(lock)*2):
        for j in range(len(lock),len(lock)*2):
            new_lock[i][j]=lock[i-len(lock)][j-len(lock)]
    
    for _ in range(4):
        key=rotation_matrix(key)
        
        for i in range(len(lock)*2):
            for j in range(len(lock)*2):
                for x in range(len(key)):
                    for y in range(len(key)):
                        new_lock[i+x][j+y]+=key[x][y]
                if check(new_lock)==True:
                    return True
                for x in range(len(key)):
                    for y in range(len(key)):
                        new_lock[i+x][j+y]-=key[x][y]
                        
    return False