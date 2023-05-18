from typing import List

def solution(temperature:List[int],A:int,B:int) -> int:
    answer = 0
    for i in range(A,B + 1):
        if temperature[i] > temperature[A] and temperature[i] > temperature[B]:
            answer += 1
    return answer

temperature : List[int] = [3, 2, 1, 5, 4, 3, 3, 2]
A : int = 1
B : int = 6
solution(temperature=temperature,A=A,B=B)