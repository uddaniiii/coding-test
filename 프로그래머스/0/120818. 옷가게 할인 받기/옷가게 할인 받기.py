def solution(price):
    if price >= 500000:
        discount = price * 0.2
    elif price >= 300000:
        discount = price * 0.1
    elif price >= 100000:
        discount = price * 0.05
    else:
        discount = 0
    
    total_price = price -discount
    return int(total_price)