from typing import List

def solution(floors: List[int]) -> int:
    dist : int = 0
    length : int = len(floors)
    
    for i in range(1,length):
        if floors[i] > floors[i-1]: 
            dist += floors[i] - floors[i-1]
        else:
            dist += floors[i-1] - floors[i]
    return dist
floors : List[int] = [1,2,5,4,2]
solution(floors=floors)