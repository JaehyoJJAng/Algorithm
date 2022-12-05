import sys
# 배열의 평균 값 

def validation_check(obj:list,type)-> list:
    if isinstance(obj,type):
        return [li for li in obj if 0 <= li <= 1000 and 1 <= len(obj) <= 100]
    else:
        print('Invalid Validation')
        sys.exit()

def solution(numbers:list):
    # Validation Check
    numbers=validation_check(obj=numbers,type=list)

    result = 0
    for val in numbers:
        result += val

    return (result / len(numbers))
