from typing import List

def solution(arr: List[int], queries: List[List[int]]) -> List[int]:
    results = []
    
    for s,e,k in queries:
        sub_arr = arr[s:e + 1]
        sub_arr.sort()
        
        answer = -1    
        for num in sub_arr:
            if num > k:
                answer = num
                break        
        results.append(answer)
    
    return results

arr : List[int] = [0,1,2,4,3]
queries : List[List[int]] = [[0, 4, 2],[0, 3, 2],[0, 2, 2]]
solution(arr=arr,queries=queries)