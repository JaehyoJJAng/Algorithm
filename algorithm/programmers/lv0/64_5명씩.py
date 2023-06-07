from typing import List

def solution(names: List[str]) -> List[str]:
    group_count = len(names) % 5    
    answer : List[str] = []
    
    for i in range(group_count):
        if i == group_count - 1:
            answer.append(names[i * 5])
        else:
            answer.append(names[i * 5])

names: List[str] = ["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]
solution(names=names)