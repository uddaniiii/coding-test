s=input()

print(*[s.find(chr(a)) for a in range(ord('a'), ord('z')+1)])
