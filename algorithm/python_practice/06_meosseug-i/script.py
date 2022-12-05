import sys
# 머쓱이보다 키 큰 사람


def validation_check(obj:list,height:int,type):
    if isinstance(obj,type) and isinstance(height,type):
        array=[arr for arr in obj if arr == int and 1 <= len(obj) <= 100 and 1 <= arr <= 200]
        if 1 <= height <= 200 and len(array) != 0:
            pass
        else:
            print('Num Error')
            sys.exit()


def solution(array:list,height:int):
    # Validation Check
    validation_check(obj=array,height=height,type=list)
    return len([x for x in array if x > height])
