s=input()

s=s.split('-')
for i in range(len(s)):
    tmp=[]
    if '+' in s[i]:
        tmp=map(int, s[i].split('+'))
        s[i]=sum(tmp)
# print(s)
res=int(s[0])
for j in s[1:]:
    # print(j)
    res-=int(j)

print(res)