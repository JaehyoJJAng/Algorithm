from typing import List

def solution(l: int,r: int) -> List[int]:
    answer = []
    for x in range(l , r + 1):
        if all(digit in "05" for digit in str(x)):
            answer.append(x)

    return answer if answer else [-1]
l : int = 5
r : int = 555
solution(l=l,r=r)