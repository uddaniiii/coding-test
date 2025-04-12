S=input()

count0=0
count1=0
# 처음 부분이 0인지 1인지 확인(0이면 1로 바꾸고 1이면 0으로 바꿔야함)
if S[0]=='0':
    count1+=1
else:
    count0+=1

# 현재 문자와 다음 문자가 다르면 다음 문자를 바꿔야한다고 가정
for i in range(1,len(S)-1):
    if S[i]!=S[i+1]:
        if S[i]=='0':
            count0+=1
        else:
            count1+=1

print(min(count0,count1))