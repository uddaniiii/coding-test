s=input()

dif=[]
for i in range(0,len(s)+1):
    for j in range(1,len(s)-i+1):
        dif.append(s[i:i+j])
print(len(set(dif)))