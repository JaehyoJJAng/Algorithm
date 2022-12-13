import sys
# 세균 증식

def validation_check(n,t,type):
    if isinstance(n,type) and isinstance(t,type):
        if 1 <= n <= 10 and 1 <= t <= 15:
            pass
        else:
            print("Num Error")
            sys.exit()
    else:
        print("Invalid Validation")
        sys.exit()

def solution(n:int,t:int):
    validation_check(n=n,t=t,type=int)
    
    for v in range(1,t+1):
        n *= 2
    return n

solution(n=2,t=10)
solution(n=7,t=15)

