import sys
import re
# 중복된 숫자 개수

def validation_check(arr:list,n:int,type)-> list:
    if isinstance(arr,type) and isinstance(n,int):
        new_arr=[new_arr for new_arr in arr if 0 <= new_arr <= 1000 and 1 <= len(arr) <= 100]
        if 0 <= n <= 1000 and len(new_arr) != 0:
            return new_arr
        else:
            print('Num Error')
            sys.exit()

""" ===== 해당 스크립트 테스트 시간 초과로 실패 =====
def solution(arr:list,n:int)-> None:
    # Validation Check
    arr=validation_check(arr=arr,n=n,type=list)
    text=re.sub('[\[\]\' ]','',str(arr))
    return text.count(str(n))
"""

def solution(arr:list,n:int)-> None:
    # Validation Check
    arr=validation_check(arr=arr,n=n,type=list)
    return arr.count(n)
