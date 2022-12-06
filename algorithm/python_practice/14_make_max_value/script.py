import sys
# 최댓값 만들기 (1)

def validation_check(obj,type)-> None:
    if isinstance(obj,type):
        arr_ch = [arr for arr in obj if 0 <= arr <= 10000]
        if 2 <= len(obj) <= 100 and len(arr_ch) != 0:
            pass
        else:
            print("Array Error")
            sys.exit()
    else:
        print("Invalid Validation")
        sys.exit()

def solution(numbers:list)-> int:
    # Validation Check
    validation_check(obj=numbers,type=list)
    
    # =====> 아래 코드 테스트 시간 초과 <=====
    #f_max=max(numbers)
    #s_max=max([num for num in numbers if num != f_max])
    #return f_max * s_max

    # =====> 풀이 (2) <=====
    numbers.sort()
    return numbers[-1] * numbers[-2]
