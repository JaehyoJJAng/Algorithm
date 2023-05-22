from typing import List

def solution(n: int,k: int) -> List[int]:
    answer : List[int] = [i for i in range(1, n + 1) if i % k == 0]
    return answer
n: int = 10
k: int = 3
solution(n=n,k=k)