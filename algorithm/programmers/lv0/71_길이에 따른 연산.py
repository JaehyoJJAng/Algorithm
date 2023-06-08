from typing import List
from math import prod

def solution(num_list: List[int]) -> int:
    answer : int = sum(num_list) if len(num_list) >= 11 else prod(num_list)
    return answer

num_list: List[int] = [3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]
solution(num_list=num_list)