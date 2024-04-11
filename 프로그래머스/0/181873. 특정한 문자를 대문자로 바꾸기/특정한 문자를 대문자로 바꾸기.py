def solution(my_string, alp):
    answer = ''
    return ''.join(i.upper() if alp==i else i for i in my_string)