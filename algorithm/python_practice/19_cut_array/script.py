# 배열 자르기


def validation_check(numbers,n1,n2,type):
    if isinstance(obj,type):
        arr_ch = [_ for _ in numbers if 0 <= _ <= 1000]
        if 2 <= len(numbers) <= 30 and arr_ch and 0 <= len(n1) < len(n2) < len(numbers):
            pass
        else:
            print("Num Error")
            sys.eixt()
    else:
        print("Invalid Validation")
        sys,exit()


def solution(numbers:list , n1:int , n2:int):
    answer = []
    n2 += 1
    return numbers[n1:n2]
