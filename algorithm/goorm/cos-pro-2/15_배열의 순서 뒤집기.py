from typing import List

def solution(arr: List[int]) -> List[int]:
    # reverse_length : int = arr[::-1]
    
    left , right = 0, len(arr) - 1
    while right > left:
        arr[left] , arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
arr : List[int] = [1,4,2,3]
solution(arr=arr)