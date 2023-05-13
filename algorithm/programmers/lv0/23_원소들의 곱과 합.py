from typing import List

def solution(num_list: List[int]) -> int:
    answer = 1
    for num in num_list:
        answer *= num
    return 1 if answer < (sum(num_list) ** 2) else 0

num_list : List[int] = [3,4,5,2,1]
print(solution(num_list=num_list))