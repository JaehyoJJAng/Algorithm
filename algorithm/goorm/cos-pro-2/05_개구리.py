from typing import List

def solution(stones: List[int]) -> int:
    cnt : int = 0
    current : int = 0
    n = len(stones)
    
    while current < n:
        current += stones[current]
        cnt += 1
    return cnt
stones : List[int] = [2,5,1,3,2,1]

print(solution(stones=stones))