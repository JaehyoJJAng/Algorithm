from typing import List 

def solution(programs: List[List[int]]) -> int:
    answer : int = 0
    used_tv = [0 for _ in range(25)]
    
    for s,e in programs:
        for i in range(s,e + 1):
            used_tv[i] += 1
            print(used_tv)
    
    for i in used_tv:
        if i >= 2:
            answer = answer + 1
    return answer       
    
programs: List[List[int]] = [[1, 6], [3, 5], [2, 8]]
ret = solution(programs)