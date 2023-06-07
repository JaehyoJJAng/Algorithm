from typing import List
def solution(num_list: List[int]) -> int:
    odd  : list[int] = sum([num_list[i] for i in range(len(num_list)) if i % 2 == 1])
    even : List[int] = sum([num_list[i] for i in range(len(num_list)) if i % 2 == 0])        
    return odd if odd > even else even
    
num_list: List[int] = [4,2,6,1,7,6]
solution(num_list=num_list)