from typing import List


def func_a(current_grade: List[int], last_grade: List[int], rank: int, max_diff_grade: int) -> int:
	arr_length : int = len(current_grade)
	count : int = 0
	for i in range(arr_length):
		if current_grade[i] >= 80 and rank[i] <= arr_length // 10:
			count += 1
		elif current_grade[i] >= 80 and rank[i] == 1:
			count += 1
		elif max_diff_grade > 0 and max_diff_grade == current_grade[i] - last_grade[i]:
			count += 1
	return count

def func_b(current_grade: List[int]) -> int:
    """ 석차 구하는 함수 """
    arr_length : int = len(current_grade)
    rank : List[int] = [1 for _ in range(arr_length)]    
    for i in range(arr_length):
        for j in range(arr_length):
            if current_grade[i] < current_grade[j]:
                rank[i] += 1 
    return rank
    
def func_c(current_grade: List[int],last_grade: List[int]) -> None:
    """ 이번 학기 - 이전 학기 성적 중 최댓값 구하는 함수 """
    max_diff_grade : int = 1
    for i in range(len(current_grade)):
        max_diff_grade = max( max_diff_grade,(current_grade[i] - last_grade[i]) )
    return max_diff_grade

def solution(current_grade: List[int],last_grade: List[int]) -> int:
    rank : int = func_b(current_grade=current_grade)
    max_diff_grade : int = func_c(current_grade=current_grade,last_grade=last_grade)
    answer = func_a(current_grade=current_grade,last_grade=last_grade,rank=rank,max_diff_grade=max_diff_grade)

current_grade : List[int] = [70, 100, 70, 80, 50, 95]
last_grade    : List[int] = [35, 65, 80, 50, 20, 60]
ret : int = solution(current_grade, last_grade)
print("solution 함수의 반환 값은", ret, "입니다.")