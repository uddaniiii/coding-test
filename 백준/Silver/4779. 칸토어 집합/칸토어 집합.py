def cantor(n):
    if n == 1:       
        return '-'
    else:
        prev = cantor(n//3) 
        return prev + ' '*(n//3) + prev
    
while True:
    try:
        n = int(input())
        print(cantor(3**n))
    except EOFError:
        break
