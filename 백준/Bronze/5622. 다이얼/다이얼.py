word=input()

dial={
    'ABC': 3,
    'DEF': 4,
    'GHI': 5,
    'JKL': 6,
    'MNO': 7,
    'PQRS': 8,
    'TUV': 9,
    'WXYZ': 10  
}

res=0
for w in word:
    for k,v in dial.items():
        if w in k:
            res+=v

print(res)