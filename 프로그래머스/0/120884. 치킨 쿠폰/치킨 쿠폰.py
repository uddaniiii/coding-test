def solution(chicken):
    coupon = 0 
    service_chicken = 0  
    
    while True:
        coupon += chicken
        service_chicken += coupon // 10
        chicken = coupon // 10
        coupon %= 10
        
        if chicken == 0:
            break
    
    return service_chicken