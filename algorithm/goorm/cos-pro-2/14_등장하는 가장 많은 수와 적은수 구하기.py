from typing import List

def func_a(arr: List[int]) -> List[int]:
    """ 1단계. 배열에 들어있는 각 자연수의 개수를 센다 """
    counter : List[int] = [0 for _ in range(1001)] 
    for x in arr:
        counter[x] += 1
    return counter
    
def func_b(arr: List[int]) -> int:
    """ 2단계. 가장 많이 등장하는 자연수의 개수를 센다 """
    ret = 0
    for x in arr:
        if ret < x:
            ret = x
    return ret

def func_c(arr: List[int]) -> int:
    """ 2단계. 가장 적게 등장하는 자연수의 개수를 센다 """
    INF = 1001
    ret = INF
    for x in arr:
        if x != 0 and ret > x:
            ret = x
    return ret

def solution(arr: List[int]) -> int:
	counter : List[int] = func_a(arr=arr)
	max_cnt : int = func_b(arr=counter)
	min_cnt : int = func_c(arr=counter)
	return max_cnt // min_cnt

arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
ret = solution(arr=arr)
print("solution 함수의 반환 값은", ret, "입니다.")