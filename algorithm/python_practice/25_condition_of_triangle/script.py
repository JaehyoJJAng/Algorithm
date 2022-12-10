import sys
# 삼각형의 완성조건 (1) 

def validation_check(obj,obj_type):
    if isinstance(obj,obj_type):
        arr_ch = [_ for _ in obj if "int" in str(type(_))]
        if len(obj) == 3 and arr_ch:
            pass
        else:
            print("Num Error")
            sys.exit()
    else:
        print("Invalid Validation")
        sys.exit()


def solution(sides:list):
    # Validation Check
    validation_check(obj=sides,obj_type=list)
    
    # 풀이 (1) : 정확성 66.7 
    #max_value = max(sides)
    #if sum([_ for _ in sides if _ != max_value]) > max_value:
        #return 1
    #else:
        #return 2
    
    # 풀이 (2) : 정확성 66.7
    #max_value = max(sides)
    #answer = 0
    #for side in sides:
        #if max_value != side:
            #answer += side
    
    #if max_value < answer:
        #return 1
    #else:
        #return 2

    # 풀이 (3)
    answer = 1  
    if sum(sides) - max(sides) <= max(sides):
        answer = 2
    return answer
