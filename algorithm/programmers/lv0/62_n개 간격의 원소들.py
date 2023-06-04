from typing import List

def solution(num_list: List[int], n: int) -> List[int]:
    answer : List[int] = num_list[::n]
    return answer

num_list : List[int] = [4,2,6,1,7,6]
n : int = 2
solution(num_list=num_list,n=n)