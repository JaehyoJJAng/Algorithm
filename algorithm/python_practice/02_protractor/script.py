import sys
# 각도기 예제

def validation_check(obj,type):
    if isinstance(obj,type):
        if 0 < obj <= 180:
            pass
        else:
            print("Num Error")
            sys.exit()
    else:
        print("Invalid Validation")
        sys.exit()

def solution(angle:int)-> None:
    validation_check(obj=angle,type=int)

    if 0 < angle < 90: # 예갹
        return 1
    elif angle == 90:  # 직각
        return 2
    elif 90 < angle < 180: # 둔각
        return 3
    else : # 평각
        return 4
