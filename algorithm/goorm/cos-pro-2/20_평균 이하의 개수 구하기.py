from typing import List

def solution(data: List[int]) -> int:
    total : int = sum(data)
    average : int = total / len(data)
    cnt : int = 0
    for d in data:
        if d < average:
            cnt += 1
    return cnt

data2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ret2 = solution(data2)

print("solution 함수의 반환 값은", ret2, "입니다.")