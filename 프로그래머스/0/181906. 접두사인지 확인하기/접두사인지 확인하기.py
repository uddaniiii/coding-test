def solution(my_string, is_prefix):

    return int(is_prefix in my_string[:len(is_prefix)])