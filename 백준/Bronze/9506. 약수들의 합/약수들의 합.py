import sys

for line in sys.stdin:
    num=[]
    if line.strip()=='-1':
        break
    for i in range(1,int(line)+1):
        if int(line)%i==0:
            num.append(i)
    if sum(num[:-1])==int(line):
        print(int(line),'=',' + '.join(map(str,num[:-1])))
    else:
        print(int(line),'is NOT perfect.')