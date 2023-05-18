from typing import List 

def solution(socks: List[int]) -> int:
    answer = 0
    
    count : List[int] = [0 for _ in range(10)]
    
    for s in socks:
        count[s] += 1
    
    for c in count:
        answer += c % 2
    return answer
    
socks : List[int] = [1,2,1,3,2,1]
solution(socks=socks)