import sys
# 순서쌍의 개수


def validation_check(obj,type):
    if isinstance(obj,type):
        if 1 <= obj <= 1000000:
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

    answer = 0
    c = len([_ for _ in range(1,n+1) if n%_ == 0])
    return c
