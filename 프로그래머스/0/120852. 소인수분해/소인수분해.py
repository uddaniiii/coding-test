def solution(n):
    factors = []  # 소인수를 저장할 리스트
    divisor = 2   # 소인수를 찾기 위한 시작값
    
    while n > 1:
        while n % divisor == 0:  # 나누어 떨어지는 경우는 소인수
            if not factors or factors[-1] != divisor:  # 중복된 소인수를 방지
                factors.append(divisor)  # 소인수를 리스트에 추가
            n //= divisor  # n을 나눈 값을 다시 n에 저장
        
        divisor += 1  # 다음 소수로 이동
    
    return factors