from typing import List
def solution(arr: List[int]) -> List[int]:
    answer : List[int] = [-1]
    index : List[int] = [i for i in range(len(arr)) if arr[i] == 2]
    return arr[index[0]:index[-1] +1] if index else answer

arr : List[int] = [1, 2, 1, 4, 5, 2, 9]
solution(arr=arr)