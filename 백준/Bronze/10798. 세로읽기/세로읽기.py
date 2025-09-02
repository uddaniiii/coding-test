chList=[input() for _ in range(5)]

# print(chList)
max_len=max(len(i) for i in chList)
res=""
for i in range(max_len):
    for j in range(5):
        if i<len(chList[j]):
            res+=chList[j][i]
print(res)