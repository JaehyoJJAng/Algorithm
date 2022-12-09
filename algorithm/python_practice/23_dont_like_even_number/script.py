import sys
# 짝수는 싫어요


def validation_check(obj,obj_type):
    if isinstance(obj,obj_type):
        if 'int' in str(type(obj)) and 1 <= obj <= 100:
            pass
        else:
            print("Num Error")
            sys.exit()
    else:
        print("Invalid Validation")
        sys.exit()


def solution(n:int):
    # Validation Check
    validation_check(obj=n,obj_type=int)
    return [_ for _ in range(1,n+1) if _ % 2 == 1]
