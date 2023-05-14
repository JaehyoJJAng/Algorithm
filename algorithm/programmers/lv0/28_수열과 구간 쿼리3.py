from typing import List

def solution(arr: List[int],queries: List[List[int]]) -> List[int]:
    # === 내 풀이 ===
    # for query in queries:
    #     a , b = arr[query[0]] , arr[query[-1]]
    #     arr[query[0]] = b
    #     arr[query[-1]] = a    
    # return arr     
    
    # === 다른 사람 풀이 ===
    for a , b in queries: # unpacking
        arr[a] , arr[b] = arr[b] , arr[a]
    return arr

arr : List[int] = [0,1,2,3,4]
queries: List[List[int]] = [[0,3] , [1,2] , [1,4]]
solution(arr=arr,queries=queries)