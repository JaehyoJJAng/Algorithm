from typing import List

def solution(votes: List[int],N: int,K: int) -> int:
    counter : List[int] = [0 for _ in range(N + 1)]    
    for x in votes:
        counter[x] += 1    
    answer = 0
    for c in counter:
        if c == K: 
            answer += 1
    return answer

votes : List[int] = [2, 5, 3, 4, 1, 5, 1, 5, 5, 3]
N : int = 5
K : int = 2
solution(votes=votes,N=N,K=K)