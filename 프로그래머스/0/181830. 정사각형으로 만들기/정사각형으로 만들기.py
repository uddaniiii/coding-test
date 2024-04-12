def solution(arr):
    num_rows = len(arr)
    num_cols = len(arr[0]) 
    

    if num_rows > num_cols:
        max_cols = num_rows
        for row in arr:
            row.extend([0] * (max_cols - len(row))) 
    

    elif num_cols > num_rows:
        max_rows = num_cols    
        for _ in range(max_rows-num_rows):
            arr.append([0] * num_cols) 
    
    return arr