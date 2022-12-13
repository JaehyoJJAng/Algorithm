import sys
# 가위바위보

def validation_check(obj,type):
    if isinstance(obj,type):
        arr_ch = [n for n in list(obj) if int(n) in [0,2,5]]
        if 0 < len(obj) <= 100 and arr_ch:
            pass
        else:
            print("Num Error")
            sys.exit()
    else:
        print("Invalid Validation")
        sys.exit()

def solution(rsp:str):
    # Validation Check
    validation_check(obj=rsp,type=str)
    
    # 풀이 (1)
#    answer = ''
#    for v in list(rsp):
#        if int(v) == 0:
#            answer += str(5)
#        elif int(v) == 2:
#            answer += str(0)
#        else :
#            answer += str(2)
#    return answer
    
    # 풀이 (2)
    d = {'0':'5','2':'0','5':'2'}
    return ''.join([d[i] for i in list(rsp)])

solution(rsp='2')
solution(rsp='205')
        
