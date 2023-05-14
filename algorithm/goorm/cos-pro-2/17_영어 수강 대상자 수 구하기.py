from typing import List

def solution(scores: List[int]) -> int:
	count : int = 0
	for s in scores:
		if 650 <= s < 800:
			count += 1
	return count

scores : List[int] = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
ret : int = solution(scores)

print("solution 함수의 반환 값은", ret, "입니다.")