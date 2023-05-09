from typing import List
def func_a(arr: List[int],n: int) -> List[int]:
    """ 배열에서 두번째로 큰 수 찾아서 리턴 """
    ret = []
    for x in arr:
        # 중복 값 제외
        if x != n:
            ret.append(x)
    return ret

def func_b(a: int,b: int) -> int:
    """ 첫 번쨰로 큰 수와 두번째로 큰 수의 차이 리턴"""
    if a >= b:
        return a - b
    else:
        return b - a

def func_c(arr: List[int]) -> int:
    """ 배열에서 가장 큰 수 찾아서 리턴 """
    ret = -1
    for x in arr:
        if ret < x:
            ret = x
    return ret

# 배열 정의
arr : List[int] = [4,7,2,9,3]

# 배열에서 가장 큰 수 추출
max_first : int = func_c(arr=arr) # 9

# 배열에서 가장 큰 수 제외
visitor_removed : List[int] = func_a(arr=arr,n=max_first)

# 배열에서 두번째로 큰 수 추출
max_second : int = func_c(arr=visitor_removed)

# 두 수 간의 차이 
result : int = func_b(a=max_first,b=max_second)