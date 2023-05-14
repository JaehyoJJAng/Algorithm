from typing import List

def solution(shirt_size: List[str]) -> List[int]:
    answer = [0 for _ in range(len(shirt_size))]
    
    for i in range(len(shirt_size)):
        if shirt_size[i] == "XS":
            answer[0] += 1
        elif shirt_size[i] == "S":
            answer[1] += 1
        elif shirt_size[i] == "M":
            answer[2] += 1
        elif shirt_size[i] == "L":
            answer[3] += 1
        elif shirt_size[i] == "XL":
            answer[4] += 1
        else:
            answer[5] += 1 
            
    return answer
shirt_size : List[str] = ["XS", "S", "L", "L", "XL", "S"]
solution(shirt_size=shirt_size)