from typing import List

def solution(price: List[int], money: int) -> int:
    answer : int = 0    
    return money - sum(price) if money >= sum(price) else -1

price : List[int] = [2100, 3200, 2100, 800]
money: int = 10000
print(solution(price=price,money=money))