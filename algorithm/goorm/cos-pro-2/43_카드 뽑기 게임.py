from typing import List

def solution(cards: List[List[str]]) -> int:
    answer = 0
    count = [0 for _ in range(3)]
    
    for card in cards:
        if card[0] == 'blue':
            count[0] += 1
        elif card[0] == 'red':
            count[1] += 1
        elif card[0] == 'black':
            count[2] += 1
        answer += int(card[-1])
    
    if count[0] == 3 or count[1] == 3 or count[2] == 3:
        answer *= 3
    elif count[0] == 2 or count[1] == 2 or count[2] ==2:
        answer *= 2
    return answer
cards : List[List[str]] = [["blue", "2"], ["blue", "5"], ["black", "3"]]
solution(cards=cards)