def solution(my_string, is_suffix):
    return int(is_suffix in my_string[-len(is_suffix):])