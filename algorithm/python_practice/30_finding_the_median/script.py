import sys
# 중앙값 구하기


def validation_check(obj,type):
    if isinstance(obj,type):
        arr_ch = [_ for _ in obj if -1000 < _ < 1000]
        if len(obj) % 2 == 1 and 0 < len(obj) < 100 and arr_ch:
            pass
        else:
            print("Num Error")
            sys.exit()
    else:
        print("Invalid Validation")
        sys.exit()

def solution(array:list):
    # Validation Check
    validation_check(obj=array,type=list)
    
    # *sorted는 반환 받을 변수가 필요
    data = sorted(array)

    centerIndex = len(data) // 2  # result : 2
    return int((data[centerIndex] + data[-centerIndex - 1]) /2)
