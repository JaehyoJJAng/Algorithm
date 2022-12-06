import sys
# 아이스 아메리카노

def validation_check(obj,type):
    if isinstance(obj,type) and 0 < obj <= 1000000:
        pass
    else:
        print("Invalid Validation")
        sys.exit()


def solution(money:int):
    # Validation Check
    validation_check(obj=money,type=int)
    
    ice_americano=5500

    # =====> 풀이 (1) <=====
    #sold=0
    #while money >= ice_americano:
        #money-= ice_americano
        #sold += 1
    #return [sold,money]

    # =====> 풀이 (2) <=====
    answer = [money // ice_americano,money % 5500]
    return answer
