import math

# n, r 입력
n, r = map(int, input().split())

# 이항 계수 계산 (math.comb() 함수 사용 가능)
print(math.comb(n, r))
