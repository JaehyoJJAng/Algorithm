from typing import List

def solution(money: int,chairs: List[int],desks: List[int]) -> None:
    answer = 0
    for chair in chairs:
        for desk in desks:
            price = chair + desk

            if answer < price and price <= money:
                answer = price
    return answer

money : int = 7
chairs : List[int] = [2,5]
desks  : List[int] = [4,3,5]
solution(money=money,chairs=chairs,desks=def)