def solution(numbers):
    maxN=max(numbers)
    numbers.remove(max(numbers))
    secN=max(numbers)
    return maxN*secN