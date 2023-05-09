from typing import List

def solution(name_list: List[str]) -> str:
    answer : int = 0
    
    for name in name_list:
        for n in name:
            if n == 'j' or n == 'k':
                answer += 1
                break
        
name_list : List[str] = ["james", "luke", "oliver", "jack"]
solution(name_list=name_list)