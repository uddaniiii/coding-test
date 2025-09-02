subject=[]
for i in range(20):
    subject.append(input().split())

score={
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

allS=0
addS=0
for n, s, g in subject:
    if g=="P":
        continue
    allS+=float(s)
    addS+=float(s)*score[g]
print(addS/allS)