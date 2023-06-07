from typing import List

def solution(numbers: List[int],n: int) -> int:
    answer = 0
    for number in numbers:
        answer += number
        if answer > n:
            break
    return answer

numbers : List[int] = [34, 5, 71, 29, 100, 34]
n : int = 123
solution(numbers=numbers,n=n)