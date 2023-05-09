from typing import List

def solution(arr: List[List[int]], k: int) -> int:
    answer : int = 0    
    arr = [j for i in arr for j in i]
    arr.sort()
    return arr[k - 1]

arr : List[List[int]] = [[5,12,4,31],[24,13,11,2],[43,44,19,26],[33,65,20,21]]
k : int = 4
print(solution(arr=arr,k=k))