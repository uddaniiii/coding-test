l = int(input())
numList = input()

MOD = 1234567891  # 문제에서 요구한 모듈러 값
BASE = 31         # 문제에서 요구한 BASE 값

res = 0
for i, n in enumerate(numList):
    n = ord(n) - ord('a') + 1  # a=1, b=2, ..., z=26
    res = (res + n * pow(BASE, i, MOD)) % MOD  # 모듈러 연산 적용

print(res)