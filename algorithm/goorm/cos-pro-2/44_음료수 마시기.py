def solution(money: int, price: int, n: int) -> int:
    answer = 0
    
    # 현재 있는 돈으로 음료수를 다 삼s
    empty_bottle = money // price
        
    while n <= empty_bottle:
        empty_bottle = empty_bottle - n
        answer += 1
        empty_bottle += 1
    
money1 = 8
price1 = 2
n1 = 4
ret1 = solution(money1, price1, n1)