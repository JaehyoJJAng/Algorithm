from typing import List

def solution(arr, query):
    s,e = 0,len(arr)
    
    for i in range(len(query)):
        if i % 2:
            s += query[i]
        else:
            e = s+query[i]
    return arr[s: e + 1] if s != 0 else [-1]
    
arr : List[int] = [0,1,2,3,4,5]
query : List[int] = [4,1,2]
solution(arr=arr,query=query)