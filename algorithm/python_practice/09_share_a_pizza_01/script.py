import sys
# 피자 나눠먹기 (1)

def validation_check(obj,type)-> None:
    if isinstance(obj,type) and 1 <= obj <= 100:
        pass
    else:
        print("Invalid Validation")
        sys.exit()

def solution(n:int):
    # Validation Check
    validation_check(obj=n,type=int)
    piece = 7 
    return (n // piece) if (n % piece) == 0 else (n // piece) + 1
