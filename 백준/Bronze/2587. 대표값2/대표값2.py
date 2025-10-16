nArr=[]
for _ in range(5):
    nArr.append(int(input()))
print(sum(nArr)//len(nArr), sorted(nArr)[2])