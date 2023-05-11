from typing import List

def solution(start: int, end: int) -> List[int]:
    answer : List[int] = [i for i in range(start, end - 1 , -1)]
    return answer    

start : int = 10
end   : int = 3
solution(start=start,end=end)