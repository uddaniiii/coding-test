T=int(input())

for i in range(T):
    h, w, n = map(int, input().split())

    floor = n % h
    if floor == 0:
        floor = h
        room = n // h
    else:
        room = n // h + 1
    
    print(f"{floor}{room:02d}")