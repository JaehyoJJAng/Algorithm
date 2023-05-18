from typing import List

def solution(people: List[int]) -> int:
    answer : List[int] = [0 for _ in range(len(people) - 1)]
    
    for i in range(len(people)):
        if people[i] < 95:
            answer[0] += 1
        elif 95<= people[i] < 100:
            answer[1] += 1
        elif 100 <= people[i] < 105:
            answer[2] += 1
        else:
            answer[3] += 1
    return answer
people : List[int] = [97, 102, 93, 100, 107]
solution(people=people)