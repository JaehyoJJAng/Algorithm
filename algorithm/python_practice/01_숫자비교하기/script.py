"""
숫자 비교하기
Author : GitHub <yshrim12@naver.com>
"""

import sys
def validation_check(obj,type):
    if isinstance(obj,type):
        if 0 <= obj <= 10000:
            pass
        else :
            print("Num Error")
            sys.exit()
    else:
        print("Invalid validation")
        sys.exit()
    

def solution(num1,num2):
    validation_check(obj=num1,type=int)
    validation_check(obj=num2,type=int)

    answer = 0
    if num1 == num2:
        return 1
    else:
        return -1
