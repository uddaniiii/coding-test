def solution(str_list):
    left_result = [] 
    right_result = [] 
    
    if "l" in str_list:
        left_index = str_list.index("l")
    else:
        left_index = float('inf')
    
    if "r" in str_list:
        right_index = str_list.index("r")
    else:
        right_index = float('inf')
    
    if left_index < right_index:
        left_result = str_list[:left_index]
    elif right_index < left_index:
        right_result = str_list[right_index+1:]
    
    return left_result if left_result else right_result