import sys
# 옷가게 할인 받기


def validation_check(obj,type):
    if isinstance(obj,type):
        if 10 <= obj <= 1000000:
            pass
        else:
            print("Num Error")
            sys.exit()
    else:
        print("Invalid Validation")
        sys.exit()

def solution(price:int):
    # Validation Check
    validation_check(obj=price,type=int)
    
    # 풀이 (1)
#    if price >= 500000:
#        return int(price * 0.8)
#    if price >= 300000:
#        return int(price * 0.9)
#    if price >= 100000:
#        return int(price * 0.95)
#    return price
    
    # 풀이 (2)
    discount_rates = {500000 : 0.8 , 300000 : 0.9 , 100000 : 0.95 , 0: 1}
    
    for discount_price , discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)
