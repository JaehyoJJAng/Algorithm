from typing import List

def solution(arr: List[int], intervals: List[List[int]]) -> List[int]:
    answer : List[List[int]] = []
    for s,t in intervals:
        answer.append(arr[s:t+1])
    return [item for x in answer for item in x]

arr : List[int] = [1,2,3,4,5]
intervals: List[List[int]] = [ [1,3] , [0,4] ]
solution(arr=arr,intervals=intervals)