pieces=[1,1,2,2,2,8]

array=list(map(int, input().split()))

print(*list(pieces[i] - array[i] for i in range(len(pieces))))