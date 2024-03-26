import math

def solution(n):
    root = math.isqrt(n)
    if root * root == n: 
        return 1
    else:
        return 2