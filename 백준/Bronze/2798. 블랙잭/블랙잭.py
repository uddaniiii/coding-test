from itertools import combinations

n,m= map(int, input().split())
n_list=list(map(int,input().split()))

comb_list=[]
for comb in combinations(n_list,3):
    if sum(comb) <= m: 
        comb_list.append(sum(comb))
print(max(comb_list))