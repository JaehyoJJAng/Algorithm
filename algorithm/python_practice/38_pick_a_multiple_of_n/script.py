import sys
# n의 배수 고르기

def validation_check(obj,type):
    if isinstance(obj,type):
        pass
    else:
        pritn("Invalid Validation")
        sys.exit()

def solution(n:int,numlist:list):
    validation_check(obj=n,type=int)
    validation_check(obj=numlist,type=list)

    return [s for s in numlist if s % n == 0]
