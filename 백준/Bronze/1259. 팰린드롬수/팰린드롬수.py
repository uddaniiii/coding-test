import sys

for line in sys.stdin:
    line = line.strip()
    if line=='0':
        break
    print("yes" if line[:] == line[::-1] else "no")