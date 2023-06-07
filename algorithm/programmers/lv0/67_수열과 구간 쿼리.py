from typing import List

def solution(arr: List[int], queries: List[List[int]]) -> List[int]:
    for s,e in queries:
        for i in range(s , e + 1):
            arr[i] += 1
    return arr        

arr : List[int] = [0,1,2,3,4]
queries: List[List[int]] = [ [0,1] , [1,2], [2,3] ]
solution(arr=arr,queries=queries)