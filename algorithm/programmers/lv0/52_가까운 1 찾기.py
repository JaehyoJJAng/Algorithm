from typing import List

def solution(arr: List[int],idx: int) -> int:
    answer = 0
    
    for i , value in enumerate(arr):
        if i >= idx:
            if value == 1:
                answer = i
                break
    else:
        answer = -1
    return answer

arr : List[int] = [0,0,0,1]
idx : int = 1
solution(arr=arr,idx=idx)