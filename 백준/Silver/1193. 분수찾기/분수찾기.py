x=int(input())

k=1
while k*(k+1)//2<x:
    k += 1
# print(k)

end=k*(k+1)//2
idx=x-end+k
# print(idx)
if k%2==1:
    up=k-idx+1
    down=idx
else:
    up=idx
    down=k-idx+1
print(f"{up}/{down}")