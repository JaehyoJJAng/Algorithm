import sys
# 배열 뒤집기

def validation_check(obj:list,type):
    if isinstance(obj,type):
        arr_ch=[arr for arr in obj if 0 <= arr <= 1000]
        if 1 <= len(obj) <= 1000 and len(arr_ch) != 0:
            pass 
        else:
            print("Num Error")
            sys.exit()
    else:
        print("Invalid Validation")
        sys.exit()

def solution(num_list:list):
    # Validation Check
    validation_check(obj=num_list,type=list)
    
    num_list.reverse()
    return num_list
