s=input()
q=int(input())
for _ in range(q):
    a,l,r=input().split()
    l=int(l)
    r=int(r)
    print(s[l:r+1].count(a))

