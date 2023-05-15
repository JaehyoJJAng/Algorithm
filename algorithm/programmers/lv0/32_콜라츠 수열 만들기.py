from typing import List

def solution(n: int) -> List[int]:
    answer : List[int] = [n]    
    while n > 1:
        n = (n // 2) if n % 2 == 0 else (3 * n + 1)
        answer.append(n)    
    return answer
n : int = 10 
solution(n=n)