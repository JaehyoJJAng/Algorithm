from typing import List
def solution(scores: List[int]) -> int:
    """
    grade_counter[0] : A
    grade_counter[1] : B
    grade_counter[2] : C
    grade_counter[3] : D
    grade_counter[4] : F
    """
    grade_counter : List[int] = [0 for i in range(5)]
    for x in scores:
        if 85 <= x <= 100:
            grade_counter[0] += 1
        elif 70 <= x <= 84:
            grade_counter[1] += 1
        elif 55 <= x <= 69:
            grade_counter[2] += 1
        elif 40 <= x <= 54:
            grade_counter[3] += 1
        else:
            grade_counter[4] += 1
    return grade_counter

scores : List[int] = [86,72,98,60,45]
solution(scores=scores)