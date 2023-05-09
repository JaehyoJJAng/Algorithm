from typing import List

def solution(height: List[int], k: int) -> int:
    answer : int = 0
    n : int = len(height)
    for h in height:
        if h > k:
            answer += 1
    return answer

height : List[int] = [165, 170, 175, 180, 184]
k : int = 175
print(solution(height=height,k=k))