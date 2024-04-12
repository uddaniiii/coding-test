def solution(n):
    ternary = ''
    while n > 0:
        ternary = str(n % 3) + ternary
        n //= 3
    
    reversed_ternary = ternary[::-1]
    decimal = int(reversed_ternary, 3)
    
    return decimal