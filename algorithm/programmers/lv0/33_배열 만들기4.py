from typing import List

def solution(arr: List[int]) -> List[int]:
    i : int = 0
    stk : List[int] = []
    while i < len(arr):
        if not stk:
            stk.append(arr[i])
            i += 1
        elif stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        elif stk[-1] >= arr[i]:
            stk.pop()
    return stk
        
arr : List[int] = [1,4,2,5,3] 
solution(arr=arr)