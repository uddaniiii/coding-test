def solution(numbers):
    an=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    dn=[0,1,2,3,4,5,6,7,8,9]
    for a,d in zip(an,dn):
        if a in numbers:
            numbers=numbers.replace(a,str(d))
    return int(numbers)