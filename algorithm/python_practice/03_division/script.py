import sys
# 두 수의 나눗셈

def validation_check(obj,type):
    if isinstance(obj,type):
        if 0 < obj <= 100:
            pass
        else:
            print("Num Error")
            sys.exit()
    else:
        print("Invalid Validation")
        sys.exit()

def solution(num1:int,num2:int):
    # Valication Check
    validation_check(obj=num1,type=int)
    validation_check(obj=num2,type=int)

    answer=0

    return int((num1 / num2) * 1000)

# Print
print(solution(num1=3,num2=2))
print(solution(num1=7,num2=3))
print(solution(num1=1,num2=16))
