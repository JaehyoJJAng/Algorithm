import sys
# 점의 위치 구하기

def validation_check(obj,type):
    if isinstance(obj,type) and len(obj) == 2:
        arr_ch = [_ for _ in obj if -500 <= _ <= 500]
        if arr_ch:
            pass
        else:
            print("Num Error")
            sys.exit()
    else:
        print("Invalid Validation")
        sys.exit()

def solution(dot:list):
    x,y = dot

    if x > 0 and  y > 0 :
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and  y < 0 :
        return 3
    else:
        return 4

print(solution(dot=[2,4]))
print(solution(dot=[-7,9]))
