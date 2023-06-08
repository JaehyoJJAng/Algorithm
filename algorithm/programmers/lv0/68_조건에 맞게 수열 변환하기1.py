from typing import List

def solution(arr: List[int]) -> List[int]:
    answer : List[int] = []
    for x in arr:
        if x >= 50 and x % 2 == 0:
            answer.append(int(x / 2))
        elif x < 50 and x % 2 == 1:
            answer.append(x * 2)
        else:
            answer.append(x)
    return answer
arr : List[int] = [1,2,3,100,99,98]
solution(arr=arr)