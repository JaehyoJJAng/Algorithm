from typing import List

def solution(purchase: List[int]) -> int:
    total : int = 0
    
    for p in purchase:
        if p >= 1000000:
            total += 50000
        elif p >= 600000:
            total += 30000
        elif p >= 400000:
            total += 20000
        elif p >= 200000:
            total += 10000
    
    return total
purchase : List[int] = [150000, 210000, 399990, 990000, 1000000]
solution(purchase=purchase)