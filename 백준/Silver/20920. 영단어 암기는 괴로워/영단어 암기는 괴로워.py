import sys
from collections import Counter

input = sys.stdin.readline
n, m = map(int, input().split())

words = []
for _ in range(n):
    w = input().rstrip()
    if len(w) >= m:
        words.append(w)

cnt = Counter(words)
# print(cnt)

sorted_words = sorted(cnt.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, _ in sorted_words:
    print(word)