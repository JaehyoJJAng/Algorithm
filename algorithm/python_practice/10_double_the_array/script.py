import sys
# 배열 두 배 만들기

def validation_check(obj:list,type):
    if isinstance(obj,type):
        arr_ch=[arr for arr in obj if -10000 <= arr <= 10000]
        if 1 <= len(obj) <= 1000 and len(arr_ch) != 0:
            pass
        else:
            print("Num Error")
            sys.exit
    else:
        print("Invalid Validation")
        sys.exit()

def solution(numbers:list):
    # Validation Check
    validation_check(obj=numbers,type=list)

    return [num * 2 for num in numbers]
