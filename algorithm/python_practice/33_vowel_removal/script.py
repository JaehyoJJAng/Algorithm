import sys
import re
# 모음 제거

def validation_check(obj,type):
    if isinstance(obj,type):
        if 1 <= len(obj) <= 1000:
            pass
        else:
            print("Num Error")
            sys.exit()
    else:
        print("Invalid Validation")
        sys.exit()

def solution(my_string:str):
    # Validation Check
    validation_check(obj=my_string,type=str)
    return ''.join([v for v in list(my_string) if v not in ['a','e','i','o','u']])

