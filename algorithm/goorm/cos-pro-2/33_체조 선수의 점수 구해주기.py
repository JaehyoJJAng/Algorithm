from typing import List 

def solution(scores: List[int]) -> int:
    if_scores : List[int] = [max(scores),min(scores)]
    answer    : List[int] = [score for score in scores if score not in if_scores]
    return int( sum(answer) / len(answer) )
    
scores : List[int] = [35, 28, 98, 34, 20, 50, 85, 74, 71, 7]
print(solution(scores=scores))