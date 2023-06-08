from typing import List

def solution(num_list: List[int]) -> int:
    add_count : int = 0
    for x in num_list:
        while x > 1:
            if x % 2 == 0:
                x /= 2
            else:
                x = (x - 1) / 2
            add_count += 1
    return add_count
num_list: List[int] = [12,4,15,1,14]
solution(num_list=num_list)