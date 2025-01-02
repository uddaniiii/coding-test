import math

n = int(input())
n_list = list(map(int, input().split()))

res = 0
for i in n_list:
    is_prime = True  # 각 숫자에 대해 소수 판별을 새로 시작
    if i < 2:  # 2보다 작은 수는 소수가 아님
        is_prime = False
    else:
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:  # 나누어떨어지면 소수가 아님
                is_prime = False
                break  # 더 이상 확인할 필요 없음
    if is_prime:
        res += 1  # 소수일 경우 개수 증가

print(res)
