import sys
import re
# 대문자와 소문자

def validation_check(obj,type):
    if isinstance(obj,type):
        if 1 <= len(obj) <= 1000:
            pass
        else:
            print("String Error")
            sys.exit()
    else:
        print("Invalid Validation")
        sys.exit()

def solution(my_string:str):
    validation_check(obj=my_string,type=str)
    
    # 풀이 (1)
#    answer = ''
#    for s in list(my_string):
#        if re.match('[a-z]',s):
#            answer += s.upper()
#        else:
#            answer += s.lower()
#    return answer

    # 풀이 (2)
#    for i in list(my_string):
#        if i.isupper():
#            answer += i.lower()
#        else:
#            answer += i.upper()
#    return answer
    
    # 풀이 (3)
    return my_string.swapcase()
print(solution(my_string='cccCCC'))
