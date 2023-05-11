from typing import List

def solution(mylist: List[int]) -> List[int]:
    answer = [(v ** 2) for v in mylist if (v % 2) == 0]
    return
    
solution(mylist=[3,2,6,7])