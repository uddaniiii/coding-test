import math
def solution(n):
    for i in range(12):
        if math.factorial(i)>n:
            return i-1
