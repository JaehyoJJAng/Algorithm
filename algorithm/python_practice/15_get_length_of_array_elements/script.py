import sys
# 배열 원소의 길이

def validation_check(obj,type):
    if isinstance(obj,type):
        arr_ch=[arr for arr in obj if 1 <= len(arr) <= 100]
        if len(arr_ch) != 0 :
            pass
        else:
            print("strlist Error")
            sys.exit()
    else:
        print("Invalid Validation")
        sys.exit()

def solution(strlist:list)-> list:
    # Validation Check
    validation_check(obj=strlist,type=list)

    return [len(st) for st in strlist]
