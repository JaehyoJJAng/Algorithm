import sys
# 짝수/홀수 개수 구하기

def validation_check(obj,type):
    if isinstance(obj,type):
        arr_ch=[arr for arr in obj if 0 <= arr <= 1000]
        if 1 <= len(obj) <= 100 and len(arr_ch) != 0:
            pass
        else:
            print("Num Error")
            sys.exit()
    else:
        print("Invalid Validation")
        sys.exit()

def solution(num_list:list)-> list:
    # Validation Check
    validation_check(obj=num_list,type=list)
    

    # =====> 풀이 (1) <=====
    #even=[num for num in num_list if (num % 2 == 0)]
    #odd=[num for num in num_list if (num % 2 != 0)]
    #return [len(even),len(odd)]

    # =====> 풀이 (2) <=====
    answer = [0,0]
    for n in num_list:
        answer[n%2]+= 1

    return answer
