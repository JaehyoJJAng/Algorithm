import sys
# 자릿수 더하기


def validation_check(obj,obj_type):
    if isinstance(obj,obj_type):
        if "int" in str(type(obj)) and 0 <= obj <= 1000000:
            pass
        else:
            print("Num Error")
            sys.exit()
    else:
        print("Invalid Validation")
        sys.exit()


def solution(n:int):
    # Check Validation
    validation_check(obj=n,obj_type=int)

    answer = 0

    return sum([int(_) for _ in list(str(n))])
