from typing import List

def solution(num_list: List[int]) -> int:
    answer = -1
    for i,x in enumerate(num_list):
        if x < 0:
            answer = i  
            break  
    return answer

num_list : List[int] = [12, 4, 15, 46, 38, -2, 15]
solution(num_list=num_list)