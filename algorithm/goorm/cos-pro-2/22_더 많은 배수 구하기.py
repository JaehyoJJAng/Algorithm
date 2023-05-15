from typing import List

def func_a(arr: List[int]) -> int:
    """ 5의 배수를 찾는 함수 """
    count : int = sum([n for n in arr if n % 5 == 0])
    return count

def func_b(three: int, five: int) -> str:
    """ 3의 배수와 5의 배수 갯수 비교하는 함수 """
    if three > five:
        return "three"
    elif three < five:
        return "five"
    else:
        return "same"
    
def func_c(arr: List[int]) -> int:
    """ 3의 배수를 찾는 함수 """
    count : int = sum([n for n in arr if n % 3 == 0])
    return count

def solution(arr: List[int]) -> str:
    count_three : int = func_c(arr=arr)
    count_five : int = func_a(arr=arr)
    answer : str = func_b(three=count_three,five=count_five)
    return answer

arr : List[int] = [2, 3, 6, 9, 12, 15, 10, 20, 22, 25]
ret : str = solution(arr)

print("solution 함수의 반환 값은", ret, "입니다.")