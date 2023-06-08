from typing import List

def perform_operation(arr: List[int]) -> List[int]:
    new_arr = arr[:]
    for i in range(len(new_arr)):
        if new_arr[i] >= 50 and new_arr[i] % 2 == 0:
            new_arr[i] //= 2
        elif new_arr[i] < 50 and new_arr[i] % 2 != 0:
            new_arr[i] = new_arr[i] * 2 + 1
    return new_arr

def solution(arr: List[int]) -> int:
    x = 0
    while True:
        new_arr = perform_operation(arr)
        if new_arr == arr:
            break
        x += 1
        arr = new_arr
    return x

arr : List[int] = [1,2,3,100,99,98]
solution(arr=arr)