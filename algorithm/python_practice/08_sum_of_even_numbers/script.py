import sys
# 짝수의 합

def validation_check(obj,type)-> None:
    if isinstance(obj,type):
        if 0 < obj <= 1000:
            pass
        else:
            print("Num Error")
            sys.exit()
    else:
        print("Invalid Validation")
        sys.exit()

def solution(n:int):
    # Validation Check
    validation_check(obj=n,type=int)

    nums=[num for num in range(1,n+1) if num%2 != 1]
    return sum([num for num in nums])
