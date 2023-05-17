from typing import List

def solution(intStrs: List[str], k: int, s: int, l: int) -> List[int]:
    answer : List[int] = []
    
    for intStr in intStrs:
        d : int = int(intStr[s:][:l])
        if k < d:
            answer.append(d)
    return answer

intStrs : List[str] = ["0123456789","9876543210","9999999999999"]	
k : int = 50000
s : int = 5 
l : int = 5
solution(intStrs=intStrs,k=k,s=s,l=l)