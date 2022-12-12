import sys
import re
# 숨어있는 숫자의 덧셈 (1)

def validation_check(obj,type):
    if isinstance(obj,type):
        if 1 <= len(obj) <= 1000:
            pass
        else:
            print("Num Error")
            sys.exit()
    else:
        print("Invalid Validation")
        sys.exit()


def solution(my_string:str):
    # Check Validation
    validation_check(obj=my_string,type=str)
    
    # 풀이 (1)
#    answer = 0
#    for n in list(my_string):
#        try:
#            answer += int(n)
#        except:
#            pass
#    return answer
    
    # 풀이 (2)
    # return sum([int(n)for n in list(re.sub('[^1-9]','',my_string)])

    # 풀이 (3)
    return sum([int(i) for i in my_string if i.isdigit()])

