import sys
# 문자열 뒤집기

def validation_check(obj,type):
    if isinstance(obj,type) and 1 <= len(obj) <= 1000:
        pass
    else:
        print("Invalid Validation")
        sys.ext()

def solution(my_string:str):
    # Validation Check
    validation_check(obj=my_string,type=str)

    # =====> 풀이 (1) <=====
    #return my_string[::-1]

    # =====> 풀이 (2) <=====
    answer=''
    string=[]

    for x in range(len(my_string)):
        string.append(my_string[x])

    string.reverse()

    for i in string:
        answer += i
    return answer
