N=int(input())
stages = list(map(int, input().split()))

total = len(stages)
result = []

for stage in range(1, N + 1):
    num = stages.count(stage)
    if total == 0:
        failure = 0
    else:
        failure = num / total
    result.append((stage, failure))
    total -= num

result.sort(key=lambda x: (-x[1], x[0]))
print([stage for stage, _ in result])