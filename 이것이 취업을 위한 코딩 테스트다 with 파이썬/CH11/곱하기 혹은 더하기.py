S=input()
res=int(S[0])
# print(fir)

for i in range(1,len(S)):
    num=int(S[i])
    if res<=1 or num<=1: # 곱한 결과나 곱할 값이 0이나 1이면 더하는게 더 최대값
        res+=num
    else:
        res*=num
print(res)