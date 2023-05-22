from typing import List

def solution(my_string: str) -> List[int]:
    count = [0 for _ in range(52)]

    for char in my_string:
        if 'A' <= char <= 'Z':
            count[ord(char) - ord('A')] += 1
        elif 'a' <= char <= 'z':
            count[ord(char) - ord('a') + 26] += 1
    
    return count
my_string: str = "Programmers"
solution(my_string=my_string)