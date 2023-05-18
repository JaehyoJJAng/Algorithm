from typing import List

def solution(papers: List[int],K: int) -> int:
    for i , paper in enumerate(papers):                
        K -= paper        
        if K < 0:
            length = i
            break
    return length
            
papers : List[int] = [2,4,3,2,1]
K : int = 10 
solution(papers=papers,K=K)