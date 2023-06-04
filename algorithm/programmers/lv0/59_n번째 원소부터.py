from typing import List

def solution(num_list: List[int],n: int) -> List[int]:
    answer : List[int] = num_list[n - 1:]
    return answer

num_list: List[int] = [5, 2, 1, 7, 5]
n : int = 2
solution(num_list=num_list,n=n)