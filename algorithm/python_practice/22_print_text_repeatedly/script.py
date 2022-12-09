import re
import sys
# 문자 반복 출력하기


def validation_check(obj,obj_type):
    if isinstance(obj,obj_type):
        if "str" in str(type(obj)) and 2 <= len(obj) <= 5:
            pass
        elif "int" in str(type(obj)) and 2 <= obj <= 10:
            pass
        else:
            print("Num Error")
            sys.exit()
    else:
        print("Invalid Validation")
        sys.exit()

def solution(my_string:str,n:int):
    # Valication Check
    validation_check(obj=my_string,obj_type=str)
    validation_check(obj=n,obj_type=int)

    return ''.join([v * n for v in list(my_string)])
