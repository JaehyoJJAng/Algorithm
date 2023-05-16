from typing import List

def solution(member_age: List[int],transportation: str) -> int:
    adult_expense : int = 0
    child_expense : int = 0
    if transportation == 'Bus':
        adult_expense  = 40000
        child_expense  = 15000
    elif transportation == 'Ship':
        adult_expense  = 30000
        child_expense  = 13000
    else :
        adult_expense  = 70000
        child_expense  = 45000

    # 여행객들이 10명 이상인 경우 연령에 따른 할인율 적용
    if len(member_age) >= 10:
        adult_expense = adult_expense * 0.9
        child_expense = child_expense * 0.8
    
    total_expense : int = 0
    for age in member_age:
        if age >= 20:
            total_expense += adult_expense
        else:
            total_expense += child_expense
    
    return int(total_expense)
    
member_age : List[int] = [25, 11, 27, 56, 7, 19, 52, 31, 77, 8]
transportation : str = "Ship"
solution(member_age, transportation)