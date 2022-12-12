import sys
# 개미 군단

def validation_check(obj,type):
    if isinstance(obj,type):
        if 0 <= obj <= 1000:
            pass
        else:
            print("Num Error")
            sys.exit()
    else:
        print("Invalid Validation")
        sys.exit()

def solution(hp:int):
    # Validation Check
    validation_check(obj=hp,type=int)
    
    # 필요한 장군개미의 수를 먼저 구함
    answer = hp // 5

    # 장군개미를 전부 상대하고 남은 hp
    hp %= 5
    
    # 남은 hp에 필요한 병정 개미의 수를 구함
    answer += hp // 3
    hp %= 3

    answer += hp // 1
    return answer

    # OR
    # return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)
