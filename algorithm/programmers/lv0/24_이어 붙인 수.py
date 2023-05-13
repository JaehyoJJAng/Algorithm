from typing import List

def solution(num_list: List[int]) -> int:
    even : int = int(''.join([str(e) for e in num_list if e % 2 == 0]))
    odd  : int = int(''.join([str(o) for o in num_list if o % 2 == 1]))
    
    return even + odd    
num_list: List[int] = [3,4,5,2,1]
solution(num_list=num_list)