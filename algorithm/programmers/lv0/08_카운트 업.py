from typing import List

def solution(start: int, end: int) -> List[int]:
    return [i for i in range(start,end + 1)]
        
start : int = 3
end   : int = 10
solution(start=start,end=end)