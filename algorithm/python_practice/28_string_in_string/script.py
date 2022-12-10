import sys
# 문자열 안에 문자열

def validation_check(obj,type):
    if isinstance(obj,type):
        if 1 <= len(obj) <= 100:
            pass
        else:
            print("String Error")
            sys.exit()
    else:
        print("Invalid Validation")
        sys.exit()

def solution(str1:str,str2:str):
    # Validation Check
    validation_check(obj=str1,type=str)
    validation_check(obj=str2,type=str)

    answer = 2
    if str2 in str1:
        answer = 1
    return answer
