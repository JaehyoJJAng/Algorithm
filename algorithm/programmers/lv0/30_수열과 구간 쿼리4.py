from typing import List

def solution(arr: List[int],queries: List[List[int]]) -> List[int]:
    for s,e,k in queries:
        for i in range(s , e + 1):
            if i % k == 0:
                arr[i] += 1
    return arr

arr : List[int] = [0,1,2,4,3]
queries: List[List[int]] = [[0, 4, 1],[0, 3, 2],[0, 3, 3]]
solution(arr=arr,queries=queries)