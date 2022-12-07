import sys
# 리스트 각 원소의 길이 가져오기

def validation_check(obj,type):
    if isinstance(obj,type):
        arr_ch=[len(arr) for arr in obj if len(arr) != 0 and 1 <= len(arr) <= 100]

        if 1 <= len(obj) <= 100 and arr_ch:
            pass
        else:
            print("Num Error")
            sys.exit()
    else:
        print("Invalid Validation")
        sys.exit()

def solution(mylist:list):
    # Validation Check
    validation_check(obj=mylist,type=list)
    return [len(elem) for elem in mylist]
